from flask import render_template, redirect
import connexion
import flask
from user import login, register


app = connexion.App(__name__, specification_dir="./", options={"swagger_ui_cors_complete": True})
app.add_api("swagger.yml")


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/register_user", methods=["GET", "POST"])
def register_user():
    if flask.request.method == 'POST':
        name = flask.request.values.get('name')
        email = flask.request.values.get('email')
        password = flask.request.values.get('password')
        user = {
            'user_name':name,
            'user_email':email,
            'user_password':password
            }
        register(user)
        return render_template("register.html")
    else:
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login_user():
    if flask.request.method == 'POST':
        email = flask.request.values.get('email')
        password = flask.request.values.get('password')
        user = {
            "user_name":email,
            "user_password": password
            }
        if(user == None):
            return redirect("login")
        else:
            return redirect("calendar")
    else:
        return render_template("login.html")
    

@app.route("/calendar")
def calendar():
    events = []
    return render_template("calendar.html", events = events)

@app.route("/list_events")
def list_events():
    events = []
    return render_template("listEvents.html",events = events)

@app.route("/add_event")
def add_event():
    return render_template("addEvent.html")

@app.route("/event")
def view_event():
    return render_template("event.html")

@app.route("/user")
def view_user():
    user = []
    return render_template("user.html", user=user)

@app.route("/edit_user")
def edit_user():
    return render_template("edit_user.html")

@app.route("/edit_event")
def edit_event():
    return render_template("editEvent.html")

@app.route("/logout")
def logout():
    return redirect("login")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)