from flask import Flask,render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(200), nullable=False, default="News")


@app.route("/")
@app.route("/article")
@app.route("/article/<category>")
def article(category="News"):
   articles = Article.query.filter_by(category=category).all()
   return render_template("article.html", news=articles)


@app.route("/delete_article/<id>", methods=["POST"])
def delete(id):
   article = Article.query.get(id)
   db.session.delete(article)
   db.session.commit()
   return redirect("/")

@app.route("/add_article", methods=["GET","POST"])
def add_article():
   if request.method == "POST":
      title = request.form.get("title")
      content = request.form.get("content")
      image_url = request.form.get("image-url")
      category = request.form.get("category")
      print(f"!!! {title},{content},{image_url},{category}")
      article = Article(title=title, content=content,image_url=image_url, category=category)
      db.session.add(article)
      db.session.commit()
      return redirect(url_for('article',category=category))

   return render_template("add_article.html")




@app.route('/test')
def test():
    # add example
    a = Article(title="Hello Ran",content="This is a very loonnnnnnnnnggg article",image_url="https://picsum.photos/200/300")
    db.session.add(a)
    a = Article(title="Hello b",content="This is a very loonnnnnnnnnggg article",image_url="https://picsum.photos/201/300", category="Sports")
    db.session.add(a)
    
    # delete example
    # a = Article.query.get(4)    
    # db.session.delete(a)
    db.session.commit()
    return "OK"

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)

#     def __repr__(self):
#         return f'<User {self.username}>'

# @app.route('/')
# def index():
#     # Create a new user
#     user = User(username='John')
#     db.session.add(user)
#     db.session.commit()

#     # Retrieve all users
#     users = User.query.all()

#     # Display users
#     output = ''
#     for user in users:
#         output += f'Username: {user.username}<br>'
#     return output

with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True)
