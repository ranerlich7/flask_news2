import sqlite3

con = sqlite3.connect("news.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS article(title, content, image)")
cur.execute("""
INSERT INTO article (title, content, image)
VALUES ("hello this is an news article", " NEWSSSSSSS bla bla bla", "https://picsum.photos/400/300"),
("hello this is an Sports article", "Sporttttttttttttt   bla bla bla", "https://picsum.photos/400/301"),
("hello this is an Finance", "Financeeeeeeeeeee bla bla bla", "https://picsum.photos/400/302")
""")
con.commit()