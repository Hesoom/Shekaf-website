from flask import Flask, render_template, redirect, url_for, flash
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from flask_login import UserMixin, login_user, login_required, current_user, logout_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
app.config["SECRET_KEY"] = '192SD87HAKD89CQHDJQXCDAQ'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///store.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    image_url = db.Column(db.String(255))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(1000))

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    posters = Items.query.all()
    return render_template("index.html", posters=posters)

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                login_user(user)
                return redirect(url_for("home"))
            else:
                flash("Invalid email or password")
                return redirect(url_for('login'))
        else:
            flash("Email doesn't exit")
            return redirect(url_for('login'))

    return render_template("login.html", form=form)

@app.route("/signup", methods=["GET","POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():

        email = form.email.data
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered, please log in instead.")
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



@app.route("/logout")
@login_required
def logout():
    logout_user() 
    flash("You have been logged out.", "success")
    return redirect(url_for("home"))

@app.route("/poster/<poster_name>")
def poster_page(poster_name):
    
    current_poster = Items.query.filter_by(name=poster_name).first()
    return render_template("poster_page.html", poster=current_poster)

@app.route("/payment")
def payment():
    return render_template("payment.html")


if __name__ == "__main__":
    app.run(debug=True)