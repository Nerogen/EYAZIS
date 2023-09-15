from flask import Flask, render_template, request

from logic_search import find_in_dir

app = Flask("App")


@app.route("/")
def main_page():
    return render_template("main.html")


@app.route("/logical_search", methods=["POST", "GET"])
def logical_search():
    if request.method == "POST":
        return render_template("logical_search.html", result=find_in_dir(request.form["query"]))
    else:
        return render_template("logical_search.html")


@app.route("/info_about_metrix")
def info_about_metrix():
    return render_template("info_about_metrix.html")


@app.route("/help")
def help():
    return render_template("help.html")


# (('Рогожин' AND 'Мышкин') OR 'Каренина')
if __name__ == '__main__':
    app.run(debug=True)
