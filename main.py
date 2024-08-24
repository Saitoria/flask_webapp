from flask import Flask, redirect, url_for, render_template, request, session, flash   #flask is a module, Flask is a classname, redirect and url_for are functions
from datetime import  timedelta

app = Flask(__name__)
app.secret_key = "mysecretkey"
app.permanent_session_lifetime = timedelta(minutes=30)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/card")
def card():
    return  render_template("card.html", Heading="Flask app", Content="This body comes directly from the API", Names=["John","Asha","Rahma"])

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["useremail"]
        session["user"] = user
        flash("Login successfull")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("You are already logged in")
            return redirect(url_for("user"))
        else:
            return render_template("login.html")


@app.route("/user", methods=["POST","GET"])
def user():
    if "user" in session:
        user = session["user"]
        return render_template("userprofile.html", Name=user)
    else:
        flash("You are not logged in")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out, {user}", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5001"), debug=True)   #The debug=True can be removed but its used to auto refresh the app if we save
    # app.run(debug=True)   #The debug=True can be removed but its used to auto refresh the app if we save
