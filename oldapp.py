from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# init database 

con = sqlite3.connect("news.db", check_same_thread=False)
cur = con.cursor()


# starting flask app
app = Flask(__name__)


# articles = ["This is todays news", "this is world news", "this is sports"]
# @app.route("/article")
@app.route("/article/<category>")
def article(category):
#    print("CATEGORY IS",category)
   res = cur.execute(f"SELECT *,rowid FROM article WHERE Category like '%{category}%'")
   articles = res.fetchall()
   print("articles",articles)
   print(f"****{articles} ")
   return render_template("article.html", news=articles)



@app.route("/add_article", methods=["POST","GET"])
@app.route("/add_article/<id>", methods=["POST","GET"])
def add_article(id=-1):
   if request.method == "POST":
      title = request.form.get("title")
      content = request.form.get("content")
      image_url = request.form.get("image-url")
      category = request.form.get("category")
      print(f"!!! {title},{content},{image_url},{category}")
      # add new article
      if id == -1:
        res = cur.execute(f"INSERT INTO article VALUES ('{title}', '{content}', '{image_url}','{category}')")
      else:
        res = cur.execute(f"""UPDATE article SET title = '{title}', content = '{content}', 
        image='{image_url}',category='{category}' WHERE rowid={id};""")

      con.commit()
      return redirect(f'/article/{category}')

   res = cur.execute(f"SELECT *,rowid FROM article WHERE rowid={id}")
   article = res.fetchall()[0]
   print("article:",article)

   return render_template("add_article.html", article=article)

@app.route("/delete_article/<id>", methods=["POST","GET"])
def delete_article(id):
    print(f"ID IS:{id}")
    res = cur.execute(f"DELETE FROM article WHERE rowid={id};")
    con.commit()
    return redirect("/article/News")


if __name__ == '__main__':
   app.run(debug=True, port=9000)