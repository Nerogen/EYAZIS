from flask import Flask, render_template, request

from metric import start_test
from logic_search import find_in_dir
from parser1 import collect

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("main.html")


@app.route("/logical_search", methods=["POST", "GET"])
def logical_search():
    if request.method == "POST":
        return render_template("logical_search.html", result=find_in_dir(request.form["query"]))
    else:
        return render_template("logical_search.html")


@app.route("/update_base", methods=["POST", "GET"])
def update_base():
    if request.method == "POST":
        result = collect(request.form["url"], request.form["name"])
        return render_template("update_base.html", result=result)
    else:
        return render_template("update_base.html")


@app.route("/info_about_metrix", methods=["POST", "GET"])
def info_about_metrix():
    if request.method == "POST":
        result = start_test()
        return render_template("info_about_metrix.html", result=result)
    else:
        return render_template("info_about_metrix.html")

@app.route("/help")
def help():
    return render_template("help.html")


if __name__ == '__main__':
    app.run(debug=True)
