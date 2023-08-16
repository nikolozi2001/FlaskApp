from flask import Flask, render_template
from config import navigation_items

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", navigation_items=navigation_items)

@app.route("/about")
def about():
    return render_template("about.html", navigation_items=navigation_items)

@app.route("/criminals")
def criminals():
    return render_template("criminals.html", navigation_items=navigation_items)

if __name__ == "__main__":
    app.run(debug=True)
