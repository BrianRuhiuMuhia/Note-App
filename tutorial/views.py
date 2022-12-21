from flask import Blueprint,render_template,request,flash,redirect,url_for
from flask_login import current_user,login_required
from .models import Note
from . import db
views=Blueprint("views",__name__)
@views.route("/",methods=['GET','POST'])
@login_required
def home_page():
    if request.method == "POST":
        text=request.form.get("text-area")
        if text:
            new_note=Note(text=text,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note Added",category="success")
    return render_template("home.html",user=current_user)
@views.route('/delete<id>')
def delete(id):
    item=Note.query.filter_by(id=id).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("views.home_page"))