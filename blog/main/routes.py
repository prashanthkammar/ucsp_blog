from flask import Blueprint, render_template, request, flash, redirect, url_for
from blog.main.forms import MemberForm
from blog.models import Post
import json
import requests

main = Blueprint("main", __name__)


def send_to_google(firstname, lastname, email, phone, usn, branch, semester):
    payload = {
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "phone": phone,
        "usn": usn,
        "branch": branch,
        "semester": semester,
    }
    print(payload)
    url = "https://script.google.com/macros/s/AKfycbza4Lx4a1AO9Ea48C57OoqTGYq2Asqf0ipYG0R5-N8cLj2Fwpc/exec"
    requests.post(url, params=payload)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/member", methods=["GET", "POST"])
def member():
    form = MemberForm()
    if request.method == "POST" and form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        phone = form.phone.data
        usn = form.usn.data
        branch = form.branch.data
        semester = form.semester.data

        send_to_google(firstname, lastname, email, phone, usn, branch, semester)
        flash(
            " Dear {}, your registration was successful!".format(
                form.firstname.data + " " + form.lastname.data
            ),
            "success",
        )
        return redirect(url_for("main.member"))
    return render_template("member.html", form=form)


@main.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)


@main.route("/about")
def about():
    return render_template("about.html")
