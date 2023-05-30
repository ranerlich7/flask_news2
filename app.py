from flask import Flask, render_template
import sqlite3

# init database 

con = sqlite3.connect("news.db", check_same_thread=False)
cur = con.cursor()


# starting flask app
app = Flask(__name__)

# articles = ["This is todays news", "this is world news", "this is sports"]
@app.route("/")
def news():
   res = cur.execute("SELECT * FROM article")
   articles = res.fetchall()
   print(articles)
   return render_template("news.html", news=articles)

sport_articles = ["City won the premier leage", "Nadal loses a game", "Liverpool rocks"]
@app.route("/sports")
def sports():
   return render_template("sport.html", sports=sport_articles)


if __name__ == '__main__':
   app.run(debug=True, port=9000)