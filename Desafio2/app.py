from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Home.html")

@app.route("/home")
def home():
    return render_template("Home.html")

@app.route("/contato")
def contato():
    return render_template("Contato.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("Quemsomos.html")