from flask import Blueprint, request, flash, render_template
from flask_login import login_required, current_user
from . import db


views = Blueprint('views', __name__)


@views.route('/', methods=['GET','POST'])
@login_required
def pt100():
    return render_template("pt100.html", user=current_user)

@views.route('/pt100', methods=['GET','POST'])
@login_required
def pt():
    return render_template("pt100.html", user=current_user)


@views.route('/upevents', methods=['GET','POST'])
@login_required
def upevents():
    return render_template("upevents.html", user=current_user)


@views.route('/about', methods=['GET','POST'])
@login_required
def about():
    return render_template("about.html", user=current_user)


@views.route('/register', methods=['GET','POST'])
@login_required
def register():
    return render_template("register.html", user=current_user)


@views.route('/curated0', methods=['GET','POST'])
@login_required
def curated():
    return render_template("curated0.html", user=current_user)

@views.route('/curated1', methods=['GET','POST'])
@login_required
def curated1():
    return render_template("curated1.html", user=current_user)

@views.route('/curated2', methods=['GET','POST'])
@login_required
def curated2():
    return render_template("curated2.html", user=current_user)




@views.route('/curated3', methods=['GET','POST'])
@login_required
def curated3():
    return render_template("curated3.html", user=current_user)


@views.route('/periodt', methods=['GET','POST'])
@login_required
def period():
    return render_template("periodt.html", user=current_user)


@views.route('/epfor', methods=['GET','POST'])
@login_required
def epfor():
    return render_template("epfor.html", user=current_user)


@views.route('/map1', methods=['GET','POST'])
@login_required
def map1():
    return render_template("map1.html", user=current_user)


@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note =note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("notes.html", user=current_user)