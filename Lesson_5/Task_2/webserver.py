from flask import Flask, render_template, request, redirect
from datetime import datetime


app = Flask("Simple news")


@app.route("/")
def index():
    temp = open("news.txt", "r")
    text = temp.readline()
    temp.close()
    return render_template("index.html", theme=text)


@app.route("/editor")
def editor():
    return render_template("editor.html")


@app.route("/process")
def process():
    temp = open("news.txt", "a")
    temp.write("<fieldset>" + "<h2>" + request.args.get("theme") + "</h2>" + "<br>" + str(currentTime()) + "<br>"
               + "<h3>" + request.args.get("text") + "</h3>" + "</fieldset>")
    return redirect("/")


def currentTime():
    now = datetime.now()
    time = now.strftime("%D:%H:%M:%S")
    return time


app.run(host="0.0.0.0", port="2711")
