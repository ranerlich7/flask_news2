from flask import Flask, render_template, request, redirect, jsonify, url_for, make_response
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(800))
    image = db.Column(db.String(100))
    category = db.Column(db.String(50), nullable=False)

@app.route('/article')
@app.route('/article/<id>')
def index(id=None):
    if not id:
        articles = Article.query.all()
    else:
        articles = [Article.query.get(id)]
    
    a_list = []
    for article in articles:
        a_list.append({
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "image": article.image,
            "category": article.category
        })
    return jsonify(a_list if not id else a_list[0])



@app.route("/add_article", methods=["POST"])
@app.route("/add_article/<id>", methods=["PUT"])
def add_article(id=-1):
    article_json = request.get_json()
    print("** got json:{article_json}")
    title = article_json.get("title")
    content = article_json.get("content")
    image_url = article_json.get("image")
    category = article_json.get("category")
    
    print(f"!!! {title},{content},{image_url},{category}")
    # add new article
    if id == -1:
        article = Article(title=title, content=content,
                            image=image_url, category=category)
        db.session.add(article)
        db.session.commit()
        response_data = {'message': 'Resource created successfully'}
        code = 201
    else:
        article = Article.query.get(id)
        article.title = title
        article.image = image_url
        article.category = category
        article.content = content
        db.session.commit()
        response_data = {'message': 'Updated successfully'}
        code = 200

 
    # Create a Flask response with the JSON data and 201 status code
    response = make_response(jsonify(response_data), code)

    # Set the Content-Type header to application/json
    response.headers['Content-Type'] = 'application/json'

    return response


@app.route("/delete_article/<id>", methods=["DELETE"])
def delete_article(id):
    article = Article.query.get(id)
    if article:
        db.session.delete(article)
        db.session.commit()
        response_data = {'message': f'Delete successful for resource {id}'}
        response = make_response(jsonify(response_data), 204)
        # Set the Content-Type header to application/json
        response.headers['Content-Type'] = 'application/json'
        return response    
    else:
        return 'Article not found.'

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
