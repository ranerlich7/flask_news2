from flask import Flask, render_template, request, redirect
import sqlite3

# init database 

con = sqlite3.connect("news.db", check_same_thread=False)
cur = con.cursor()


# starting flask app
app = Flask(__name__)

# articles = ["This is todays news", "this is world news", "this is sports"]
@app.route("/")
def news():
   res = cur.execute("SELECT *,rowid FROM article WHERE Category='News'")
   articles = res.fetchall()
   print(f"****{articles} ")
   return render_template("article.html", news=articles)

# sport_articles = ["City won the premier leage", "Nadal loses a game", "Liverpool rocks"]
@app.route("/sports")
def sports():
   res = cur.execute("SELECT *,rowid FROM article WHERE Category='Sports'")
   articles = res.fetchall()
   print(f"****{articles} ")
   return render_template("article.html", news=articles)

@app.route("/addarticle", methods=["POST","GET"])
def addarticle():
    if request.method == "POST":
        # get parameters from form
        title = request.form.get('title')
        content = request.form.get('content') 
        print(f"!!!!!!!!!!!!! title:{title}. content:{content}")   
        # add to database
        res = cur.execute(f'INSERT INTO article VALUES ("{title}", "{content}", "https://picsum.photos/400/309","Sports")')
        con.commit()        
        return "ADDED AN ARTICLE WOOHOO!"
    else:
        return render_template("add_article.html")

@app.route("/delete_article/<id>", methods=["POST","GET"])
def delete_article(id):
    print(f"ID IS:{id}")
    res = cur.execute(f"DELETE FROM article WHERE rowid={id};")
    con.commit()
    return redirect("/")

if __name__ == '__main__':
   app.run(debug=True, port=9000)