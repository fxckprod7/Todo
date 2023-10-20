from flask import Flask, render_template, url_for, request, redirect

from db_manager import Database

db = Database("database.db")


app = Flask(__name__)


# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def index():
    shoping_tasks = db.get_shoping()
    return render_template("index.html", shoping_tasks=shoping_tasks)


@app.route('/create_shoping_item', methods=['POST', 'GET'])
def create_shoping_item():
    if request.method == 'POST':
        title = request.form.get("shoping_title")
        db.create_shoping(title)

        return redirect('/')
    else:
        return redirect('/404')


if __name__ == '__main__':
    app.debug = True
    app.run()
