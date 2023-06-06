import sqlite3
con = sqlite3.connect("news.db")
cur = con.cursor()

def init():
    cur.execute("CREATE TABLE IF NOT EXISTS article(id INTEGER PRIMARY KEY AUTOINCREMENT, title, content, image, category DEFAULT 'News')")
    cur.execute("""
    INSERT INTO article (title, content, image)
    VALUES ("hello this is an news article", " NEWSSSSSSS bla bla bla", "https://picsum.photos/400/300"),
    ("hello this is an Sports article", "Sporttttttttttttt   bla bla bla", "https://picsum.photos/400/301"),
    ("hello this is an Finance", "Financeeeeeeeeeee bla bla bla", "https://picsum.photos/400/302")
    """)
    con.commit()
    
def add_article():
    cur.execute("""
    INSERT INTO article (title, content, image, category)
    VALUES ("Sports article", "Manchester City won", "https://picsum.photos/401/300", "Sports"),
    ("Liverpool article", "Liverpool signs messi", "https://picsum.photos/402/300", "Sports")
    """)
    con.commit()
    
def add_category():
    cur.execute("ALTER TABLE article ADD Category varchar(255) DEFAULT 'News';")
    # cur.execute("ALTER TABLE article DROP COLUMN Category; ")

add_article()
# init()
# add_category()
con.commit()