import sqlite3
con = sqlite3.connect("news.db")
cur = con.cursor()
cur.execute("""
INSERT INTO article (title, content, image)
VALUES ("3333333", " 4444", "5.jpg")
""")

con.commit()