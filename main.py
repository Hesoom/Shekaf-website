from flask import Flask, render_template
import sqlite3

conn = sqlite3.connect("item.db")
c = conn.cursor()

c.execute("SELECT * FROM items")
posters = c.fetchall()


app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html", posters=posters)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/poster/<poster_name>")
def poster_page(poster_name):
    with sqlite3.connect("item.db") as con:
        c = con.cursor()
        c.execute("SELECT * FROM items WHERE name = ?", (poster_name,))
        current_poster = c.fetchall()[0]
    
    return render_template("poster_page.html", poster=current_poster)

@app.route("/payment")
def payment():
    return render_template("payment.html")

conn.close()
if __name__ == "__main__":
    app.run(debug=True)