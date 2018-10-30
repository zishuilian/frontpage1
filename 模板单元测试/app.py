# -*- coding:utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/home.html")
def home():
    return render_template("home.html")


@app.route("/login.html")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
