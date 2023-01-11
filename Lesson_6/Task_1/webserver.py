from flask import Flask, render_template, request, redirect
from dataBase import *


app = Flask("Simple chat")
prepareDataBase("users.db")


@app.route('/')
def index():
    rows = getNicknamesAndMessageFromDB("users.db")
    return render_template("index.html", users=printNicknamesAndMessages(rows))


@app.route('/register')
def register():
    nickname = request.args.get('nickname')
    message = request.args.get('message')
    enterNicknamesAndMessagesInDB("users.db", nickname, message)
    return redirect('/')


@app.route('/updatepage')
def update():
    rows = getNicknamesAndMessageFromDB("users.db")
    return printNicknamesAndMessages(rows)


app.run(host='0.0.0.0', port=2711)
