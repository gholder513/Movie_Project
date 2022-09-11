from flask import Blueprint, render_template, redirect, url_for
from app import app

views = Blueprint(__name__, "views")

@app.route("/")
def home():
    return render_template("home.html")