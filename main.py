from flask import Flask, render_template, request, jsonify
from src.convert import changeBase
from src.validate import checkInput

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", num="", fromBase="", toBase="", res="")


@app.route("/", methods=['GET', 'POST'])
def convert():
    if request.method == "POST":
        num = request.form["num"]
        fromBase = request.form["from"]
        toBase = request.form["to"]
        if checkInput(num, fromBase, toBase) != 1:
            return render_template("index.html", error="Invalid input.")
        res = changeBase(num, int(fromBase), int(toBase))
        # Print to console.
        # print("Result = " + res)
        return render_template("index.html", num=num, fromBase=fromBase, toBase=toBase, res=res)
    else:
        return render_template("index.html", num="", fromBase="", toBase="", res="")


if __name__ == "__main__":
    app.run(debug=True)
