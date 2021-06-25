from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User


@app.route("/users")
def index():
    users = User.get_all()
    print(users)
    return render_template("all_users.html", all_users = users)

@app.route("/users/new")
def inputUserInfo():
    return render_template("new_users.html")

@app.route("/create_users", methods=["POST"])
def create_user():
    data = {
        "fname": request.form["first_name"],
        "lname" : request.form["last_name"],
        "email" : request.form["user_email"]
    }
    id = User.save(data)
    # why does this  redirect hate me!
    return redirect(f"/users/{id}")

@app.route("/users/<int:id>")
def one_user(id):
    data = {
        'id' : id
    }
    user = User.get_one(data)
    return render_template("read_one.html", user = user)

# do i need get and post?
@app.route("/users/<int:id>/edit")
def go_edit(id):
    data = {
        'id' : id
    }
    user = User.get_one(data)
    return render_template("edit.html", user =user)

@app.route("/users/<int:id>/editdb", methods=["POST"])
def edit(id):
    data = {
        "fname": request.form["first_name"],
        "lname" : request.form["last_name"],
        "email" : request.form["email"],
        "id" :id
    }
    User.update_user(data)
    return redirect(f"/users/{id}")

@app.route("/users/<int:id>/delete")
def delete(id):
    data = {
        'id' : id
    }
    user = User.del_user(data)
    return redirect("/users")