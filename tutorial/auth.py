from flask import Blueprint,render_template,request,flash,redirect,url_for
from . import db
from flask_login import login_user,logout_user,current_user,login_required
from .models import User
auth=Blueprint("auth",__name__)
@auth.route("login",methods=['GET','POST'])
def login():
    if request.method == "POST":
        email=request.form.get("email")
        password=request.form.get("password")
        user=User.query.filter_by(email=email).first()
        if user:
            if password == user.password:
                flash("Logged in Successfully",category="success")
                login_user(user,remember=True)
                return redirect(url_for("views.home_page"))
            else:
                flash("Incorrect password try again",category="error")
        else:
            flash("Email does not exist",category="error")
    return render_template("login.html",user=current_user)
@auth.route("register",methods=['GET','POST'])
def register():
    if request.method == 'POST':
        fName=request.form.get("firstName")
        lName=request.form.get("lastName")
        email=request.form.get("email")
        password=request.form.get("password")
        confirmPassword=request.form.get("confirmPassword")
        if len(fName) <2:
            flash("first name must be greater than 2 characters",category="error")
        elif len(lName) <2:
            flash("last name must be greater than 2 characters",category="error")
        elif len(email) <5:
            flash("email must be greater than 5 characters",category="error")
        elif len(password) < 7:
            flash("password must be greater than 7 characters",category="error")
        elif password != confirmPassword:
            flash("password must be the same",category="error")
        else:
            if User.query.filter_by(email=email).first():
                flash("Already Registered",category="error")
                return redirect(url_for("auth.login"))
            else:
              new_user=User(fName=fName,lName=lName,email=email,password=password)
              db.session.add(new_user)
              db.session.commit()
              flash("Account Created",category="success")
              login_user(new_user,remember=True)
              return redirect(url_for("views.home_page"))
    return render_template("register.html",user=current_user)
@auth.route("logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))