from flask import Flask, render_template, request, redirect
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


# @app.route("/article")
@app.route("/article/<category>")
def article(category):
    articles = Article.query.filter(Article.category.ilike(category)).all()
    print("articles", articles)
    print(f"****{articles} ")
    return render_template("article.html", news=articles)


@app.route("/add_article", methods=["POST", "GET"])
@app.route("/add_article/<id>", methods=["POST", "GET"])
def add_article(id=-1):
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        image_url = request.form.get("image-url")
        category = request.form.get("category")
        print(f"!!! {title},{content},{image_url},{category}")
        # add new article
        if id == -1:
            article = Article(title=title, content=content,
                              image=image_url, category=category)
            db.session.add(article)
            db.session.commit()
        else:
            article = Article.query.get(id)
            article.title = title

            db.session.commit()

        return redirect(f'/article/{category}')

    article = Article.query.get(id)

    return render_template("add_article.html", article=article)


@app.route("/delete_article/<id>", methods=["POST"])
def delete_article(id):
    article = Article.query.get(id)
    if article:
        db.session.delete(article)
        db.session.commit()
        return redirect("/article/"+article.category)
    else:
        return 'Article not found.'

# @app.route('/')
# def index():
#    article = Article(title='News 22222 is here',content="Hello this is content",image="https://picsum.photos/id/137/300/200", category="News")
#    db.session.add(article)
#    article = Article(title='News 33333 is here',content="Hello this is content",image="https://picsum.photos/id/137/300/200", category="News")
#    db.session.add(article)
#    db.session.commit()


#    # Retrieve all users
#    articles = Article.query.all()


#    # Display users
#    output = ''
#    for article in articles:
#        output += f'Article: {article.title}<br>'
#    return output


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
