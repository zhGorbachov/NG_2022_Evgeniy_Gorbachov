from flask import Flask, request, render_template, redirect, send_file
from parser import *


app = Flask("Picture parser")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/parsing")
def progressing():
    url = request.args.get("url")
    parsedImages = parsingImages(url)
    downloadImages(parsedImages)
    return redirect("/download")


@app.route("/download")
def download():
    path = "F:/github/NG_2022_Evgeniy_Gorbachov/Lesson_7/images.zip"
    return send_file(path, as_attachment=True)


app.run(host="0.0.0.0", port="2711")

