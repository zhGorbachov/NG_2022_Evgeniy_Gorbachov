from flask import Flask, render_template, request


app = Flask("Simple calculator")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/calcs')
def calculating():
    firstN = float(request.args.get("firstValue"))
    secondN = float(request.args.get("secondValue"))
    match request.args.get("action"):
        case "+":
            result = firstN+secondN
            return render_template('index.html', result=result)
        case "-":
            result = firstN-secondN
            return render_template("index.html", result=result)
        case "*":
            result = firstN*secondN
            return render_template("index.html", result=result)
        case "/":
            if secondN == 0:
                return render_template("index.html", result="[Error]Division by zero!")
            result = firstN/secondN
            return render_template("index.html", result=result)
        case "%":
            result = firstN%secondN
            return render_template("index.html", result=result)


app.run(host="0.0.0.0", port="2711")
