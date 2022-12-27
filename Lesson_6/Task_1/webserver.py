from flask import Flask, render_template, request, redirect
from dataBase import *


app = Flask("Simple chat")
prepareDb("users.db")


@app.route('/')
def index():
    rows = getLogins("users.db")
    return render_template("index.html", users=printMessage(rows))


@app.route('/register')
def register():
    login = request.args.get('login')
    message = request.args.get('message')
    registerUser("users.db", login, message)
    return redirect('/')


@app.route('/updatepage')
def update():
    rows = getLogins("users.db")
    return printMessage(rows)


app.run(host='0.0.0.0', port=2711)
