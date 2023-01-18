import time

from flask import Flask, render_template, request, redirect
from datetime import datetime
import os


app = Flask("Simple news")
nameOfFile = "news.txt"
temp = open(nameOfFile, "w")


@app.route("/")
def index():
    temp = open(nameOfFile, "r")
    if os.stat(nameOfFile).st_size != 0:
        text = temp.readline()
        temp.close()
        return render_template("index.html", news=text)
    else:
        temp.close()
        return render_template("index.html")


@app.route("/editor")
def editor():
    return render_template("editor.html")


@app.route("/process")
def process():
    temp = open(nameOfFile, "a")
    temp.write("<fieldset>" + "<h2>" + request.args.get("theme") + "</h2>" + "<br>" + str(currentTime()) + "<br>"
               + "<h3>" + request.args.get("text") + "</h3>" + "</fieldset>")
    temp.close()
    print("[LOG] News wrote at: " + str(currentTime()))
    return redirect("/")


@app.route("/signUpAdmin")
def redirectToSignUp():
    return render_template("signUpAdmin.html")


@app.route("/confirmAdmin")
def confirmAdmin():
    login = request.args.get("login")
    password = request.args.get("password")

    if login == "admin" and password == "qwerty123":
        return render_template("admin.html")

    else:
        return redirect("/signUpAdmin")


@app.route("/admin")
def admin():
    match request.args.get("choose"):
        case "clear":
            temp = open(nameOfFile, "w")
            temp.close()
            print("[INFO] Admin cleared news at: " + str(currentTime()))
            return redirect("/")
        case "message":
            announcement = request.args.get("announcement")
            temp = open(nameOfFile, "r")
            text = "<h1>[Admin]---<u>" + str(announcement) + "</u></h1>" + "<br>" + str(temp.readline())
            temp.close()
            print("[INFO] Admin announced message at: " + str(currentTime()))
            return render_template("index.html", news=text)
        case "shut_down":
            temp = open(nameOfFile, "r")
            temp.close()
            print("[INFO] Admin shut down site at: " + str(currentTime()))
            time.sleep(5)
            quit()


def currentTime():
    now = datetime.now()
    time = now.strftime("%D:%H:%M:%S")
    return time


app.run(host="0.0.0.0", port="8000")
