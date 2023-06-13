from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(800))
    image = db.Column(db.String(100))
    category = db.Column(db.String(50), nullable=False)


@app.route("/article")
@app.route("/article/<id>")
def article(id=-1):
    if id == -1:
        articles = Article.query.all()
    else:
        articles = [Article.query.get(id)]
    return_data = []
    for article in articles:
        return_data.append(
            {
                'id': article.id,
                'title': article.title,
                'content': article.content,
                'image': article.image,
                'category': article.category
            })
    if id != -1:
        return jsonify(return_data[0])

    return jsonify(return_data)

# {
#   title: 'foo',
#   content: 'bar',
#   category: 'News',
#   image: ''
# }
@app.route('/create_article', methods=['POST'])
def create_article():
    data = request.get_json()
    new_article = Article(title=data['title'], content=data['content'], category=data['category'],image=data['image'])
    db.session.add(new_article)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
