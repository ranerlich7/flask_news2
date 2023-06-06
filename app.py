from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

# init database 

con = sqlite3.connect("news.db", check_same_thread=False)
cur = con.cursor()


# starting flask app
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# articles = ["This is todays news", "this is world news", "this is sports"]
@app.route("/")
def news():
   res = cur.execute("SELECT * FROM article WHERE category='News'")
   articles = res.fetchall()
   print(f"****{articles} ")
   return render_template("news.html", news=articles)

# sport_articles = ["City won the premier leage", "Nadal loses a game", "Liverpool rocks"]
@app.route("/sports")
def sports():
   res = cur.execute("SELECT * FROM article WHERE category='Sports'")
   sport_articles = res.fetchall()
   return render_template("sport.html", news=sport_articles)

@app.route("/add_article", methods=["GET","POST"])
def add_article():
   if request.method == "POST":
      title = request.form.get("title")
      content = request.form.get("content")
      image = request.form.get("image")
      category = request.form.get("category")
      print(f'{title},{content},{image},{category}')
      res = cur.execute(f'INSERT INTO article VALUES ("{title}","{content}","{image}","{category}");')
      con.commit()
      flash("Added succesfuly")
      return redirect(url_for('news'))
      
   else:
      return render_template('add_article.html')

if __name__ == '__main__':
   app.run(debug=True, port=9000)
   
