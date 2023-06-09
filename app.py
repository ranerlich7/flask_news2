from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
db = SQLAlchemy(app)




class Article(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(80), unique=True, nullable=False)
   content = db.Column(db.String(800), unique=True, nullable=False)

  
   def __repr__(self):
       return f'<User {self.username}>'


@app.route('/')
def index():
   # Create a new user
   user = User(username='Ran')
   db.session.add(user)
   db.session.commit()


   # Retrieve all users
   users = User.query.all()


   # Display users
   output = ''
   for user in users:
       output += f'Username: {user.username}<br>'
   return output


with app.app_context():
   db.create_all()

if __name__ == '__main__':
   app.run(debug=True)