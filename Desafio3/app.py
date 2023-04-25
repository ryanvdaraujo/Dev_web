from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'fatec'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("Home.html")

@app.route("/home")
def home():
    return render_template("Home.html")
'''
@app.route("/contato")
def contato():
    return render_template("Contato.html")
'''

@app.route("/contato", methods =['POST', 'GET'])
def contato():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute(f'INSERT INTO contatos(email, assunto, decricao) VALUES ("{email}", "{assunto}", "{descricao}")')

        mysql.connection.commit()

        cur.close()

        return 'Concluído'
    return render_template("Contato.html")


@app.route("/quemsomos")
def quemsomos():
    return render_template("Quemsomos.html")