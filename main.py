from flask import Flask, render_template
import sqlite3

conn = sqlite3.connect("item.db")
c = conn.cursor()

c.execute("SELECT * FROM items")
posters = c.fetchall()


app = Flask(__name__)

@app.route("/")
def hello_flask():

    return render_template("index.html", posters=posters)



conn.close()
if __name__ == "__main__":
    app.run(debug=True)