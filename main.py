from flask import Flask, render_template, request, redirect, jsonify
from src.convert import changeBase

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/convert", methods=['GET', 'POST'])
def convert():
    if request.method == "POST":
        num = request.form["num"]
        fromBase = int(request.form["from"])
        toBase = int(request.form["to"])
        return jsonify(changeBase(num, fromBase, toBase))
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
