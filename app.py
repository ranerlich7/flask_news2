from flask import Flask
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



@app.route('/')
def index():
   article = Article(title='News 22222 is here',content="Hello this is content",image="https://picsum.photos/id/137/300/200", category="News")
   db.session.add(article)
   article = Article(title='News 33333 is here',content="Hello this is content",image="https://picsum.photos/id/137/300/200", category="News")
   db.session.add(article)
   db.session.commit()


   # Retrieve all users
   articles = Article.query.all()


   # Display users
   output = ''
   for article in articles:
       output += f'Article: {article.title}<br>'
   return output


with app.app_context():
   db.create_all()

if __name__ == '__main__':
   app.run(debug=True)