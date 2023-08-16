from flask import Flask, render_template, request, redirect, url_for
from config import navigation_items

app = Flask(__name__)

users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route("/")
def home():
    return render_template("index.html", navigation_items=navigation_items)

@app.route("/about")
def about():
    return render_template("about.html", navigation_items=navigation_items)

@app.route("/criminals")
def criminals():
    return render_template("criminals.html", navigation_items=navigation_items)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return f'Logged in as {username}'
        else:
            return 'Invalid username or password'
    return render_template("login.html", navigation_items=navigation_items)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if username in users:
            return 'Username already exists'
        elif password != confirm_password:
            return 'Passwords do not match'
        else:
            users[username] = password
            return f'Registered new user: {username}'
    return render_template("register.html", navigation_items=navigation_items)


if __name__ == "__main__":
    app.run(debug=True)
