import sqlite3

con = sqlite3.connect("news.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS article(title, content, image)")
cur.execute("""
INSERT INTO article (title, content, image)
VALUES ("hello this is an news article", " NEWSSSSSSS bla bla bla", "1.jpg"),
("hello this is an Sports article", "Sport   bla bla bla", "2.jpg"),
("hello this is an Finance", "Finance bla bla bla", "3.jpg")
""")
con.commit()