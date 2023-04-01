import json
from dotenv import load_dotenv
import os
from flask import render_template, redirect, session, request, url_for
import connexion
import flask
from user import login, register_user,read_user,read_all_users,delete_user,update_user, logout
from event import create_event, read_all_events, read_event, update_event, delete_event
load_dotenv()

app = connexion.App(__name__, specification_dir="./", options={"swagger_ui_cors_complete": True})
app.add_api("swagger.yml")
app.app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')



def check_login():
    user_id = session.get('user_id')
    return user_id == ''
       
    


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/register_user", methods=["GET", "POST"])
def register_user():
    if request.method == 'POST':
        name = flask.request.values.get('name')
        email = flask.request.values.get('email')
        password = flask.request.values.get('password')
        user = {
            'user_name':name,
            'user_email':email,
            'user_password':password
            }
        register_user(user)
        return redirect("login")
    else:
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login_user():
    if request.method == 'POST':
        email = flask.request.values.get('email')
        password = flask.request.values.get('password')
        user = {
            "user_email":email,
            "user_password": password
            }
        user = json.loads(login(user).data)
        if not user:
            error = "erro ao logar"
            return render_template("login.html", error= error)
        else:
            session['user_id'] = user["user_id"]
            print("chegou")
            return redirect(url_for("calendar"))
    else:
        session['user_id'] = ''
        return render_template("login.html")
    

@app.route("/calendar")
def calendar():
    print("sesssao ", session.get("user_id"))
    print(check_login())

    if check_login():
        print("não logado redirecionado pra login")
        return redirect("login")
    
    user_id = session.get("user_id")
    events = json.loads(read_all_events(user_id=user_id).data)
    return render_template("calendar.html", events = events)

@app.route("/list_events")
def list_events():
    if check_login():
        return redirect("login")
    print(check_login())
    user_id = session.get("user_id")
    events = json.loads(read_all_events(user_id=user_id).data)
    print(events)
    return render_template("listEvents.html", events = events)

@app.route("/add_event", methods=["GET", "POST"])
def add_event(): 
    if request.method == "POST":
        event_title = flask.request.values.get('event_title')
        event_description = flask.request.values.get('event_description')
        event_date = flask.request.values.get('event_date')
        event_hour = flask.request.values.get('event_hour')
        event_date = f"{event_date} {event_hour}:00"
        event = {
            "event_title":event_title,
            "event_description":event_description,
            "event_date":event_date,
            "user_id": session.get("user_id")
            }
        create_event(event=event)
        return redirect("list_events")
    else:
        if check_login():
            return redirect("login")
        return render_template("addEvent.html")

@app.route("/event/<int:id>")
def view_event(id):
    if check_login():
        return redirect("login")
    event = json.loads(read_event(id).data)
    return render_template("event.html", event=event)

@app.route("/user")
def view_user():
    if check_login():
        return redirect("login")
    user_id = session.get("user_id")
    user = json.loads(read_user(user_id).data)
    return render_template("user.html", user=user)

@app.route("/edit_user/<int:id>")
def edit_user(id):
    if flask.request.method == "PATH":
        name = flask.request.values.get('name')
        email = flask.request.values.get('email')
        user_id = session.get("user_id")
        actual_password = flask.request.values.get('actual_password')
        user = json.loads(read_user(user_id).data)
        if(actual_password == user.user_password):
            update_user =  {
                "user_id": user_id,
                "user_name":name,
                "user_email":email
                }
            update_user(json.loads(user).data)
            return redirect("user")
    else:    
        if check_login():
            return redirect("login")
        base_url = request.url_root
        user_id = session.get('user_id')
        
        user = json.loads(read_user(user_id).data)
        return render_template("edit_user.html", user_id=user_id, base_url=base_url, user=user)

@app.route("/edit_event/<int:id>")
def edit_event(id):
    if request.method == "PATH":
        event_title = flask.request.values.get('event_title')
        event_descrition = flask.request.values.get('event_description')
        event_date = flask.request.values.get('event_date')
        event_hour = flask.request.values.get('event_hour')

        event_date = f"{event_date} {event_hour}:00"
        event = {
            "event_id": id,
            "event_title":event_title,
            "event_descrition":event_descrition,
            "event_date":event_date
            }
        update_event(event)
        return redirect("login")
    else:
        if check_login():
            return redirect("login")
        user_id = session.get('user_id')
        event = json.loads(read_event(id).data)
        base_url = request.url_root
        
        return render_template("editEvent.html", user_id=user_id, event=event, base_url=base_url)

@app.route("/logout")
def user_logout():
    logout(session.get('user_id'))
    session['user_id'] = ''
    return redirect("login")

@app.route("/del_event/<int:id>", methods=["POST"])
def event_delete(id):
    delete_event(id)
    return redirect("list_events")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)