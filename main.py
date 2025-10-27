from flask import Flask, render_template, redirect, url_for, flash
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from flask_login import UserMixin, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import os


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "item.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute("SELECT * FROM items")
posters = c.fetchall()


app = Flask(__name__)
app.config["SECRET_KEY"] = '192SD87HAKD89CQHDJQXCDAQ'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///items.db'
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(1000))

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html", posters=posters)

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        

        if form.email.data == "2@2.com" and form.password.data == 'password':
            flash(f"Successfuly Loged in",'success')
            return redirect(url_for('home'))
        else:
            flash(f"Wrong Email or Password")
    return render_template("login.html", form=form)

@app.route("/signup", methods=["GET","POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():

        email = form.email.data
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered, please log in instead.")
            print(existing_user.email)
            return redirect(url_for('login'))

        hashed_password = generate_password_hash(form.password.data,method='pbkdf2',salt_length=8)
        new_user = User(
            email=form.email.data,
            username=form.username.data,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        flash(f"Account created",'success')
        return redirect(url_for('home'))
    
    return render_template("signup.html", form=form)

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