from flask import Flask, url_for, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from random import randint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']="my-secret-key-hehe"

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return self.name


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __str__(self):
        return self.name

@app.route("/")
def index():
    preco = randint(100,200)
    return render_template("index.html", valor = preco)

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")
    
@app.route("/pagamentos")
def pagamentos():
    return render_template("pay.html")

@app.route("/rastreio")
def rastreio():
    return render_template("rastreio.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        user = request.form['user']
        password = request.form['password']
    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True, host="localhost", port=5500)