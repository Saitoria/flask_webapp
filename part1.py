from flask import Flask, redirect, url_for, render_template   #flask is a module, Flask is a classname, redirect and url_for are functions

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello this is a mini page <h1> Flask app </h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home")) #takes in the function not route

@app.route("/manager")
def manager():
    return redirect(url_for("user", name="Manager!"))

if __name__ == "__main__":
    app.run()