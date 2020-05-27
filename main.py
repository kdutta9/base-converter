from flask import Flask, render_template, request, jsonify
from src.convert import changeBase

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    # do something
    pass


if __name__ == "__main__":
    app.run(debug=True)
