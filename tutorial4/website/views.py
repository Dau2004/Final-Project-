from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User
from . import db
from .form import ScheduleCollectionForm, TrackRecyclingForm

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
    schedule = ScheduleCollectionForm()
    track = TrackRecyclingForm()
    return render_template("home.html", user=current_user, schedule=schedule, track=track)

@views.route("/")
@views.route("/schedule")
@login_required
def schedule():
    return render_template("schedule.html", user=current_user)

@views.route("/")
@views.route("/recycle")
@login_required
def recycle():
    return render_template("recycle.html", user=current_user)

@views.route("/")
@views.route("/admin")
@login_required
def admin():
    return render_template("admin.html", user=current_user)


