from flask import Flask, render_template, request, redirect
from configuration import *
from dataBase import *


app = Flask("Configuration of PC")
prepareDataBase("configuration.db")


@app.route("/")
def index():
    rows = getInformation("configuration.db")
    return render_template("index.html", info=printInformationFromBase(rows))


@app.route("/process")
def processing():
    list = request.args.getlist("configuration")
    process("configuration.db", list)
    return redirect("/")


app.run(host="0.0.0.0", port=2711)
