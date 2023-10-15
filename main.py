from flask import Flask, render_template, url_for, request, redirect

from db_manager import Database

db = Database("database.db")


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=5050)
