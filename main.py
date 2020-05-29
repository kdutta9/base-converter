from flask import Flask, render_template, request, jsonify
from src.convert import changeBase

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", num="", fromBase="", toBase="", res="")


@app.route("/", methods=['GET', 'POST'])
def convert():
    if request.method == "POST":
        num = request.form["num"]
        fromBase = int(request.form["from"])
        toBase = int(request.form["to"])
        res = changeBase(num, fromBase, toBase)
        print("Result = " + res)
        return render_template("index.html", num=num, fromBase=fromBase, toBase=toBase, res=res)
    else:
        return render_template("index.html", num="", fromBase="", toBase="", res="")


if __name__ == "__main__":
    app.run(debug=True)
