from flask import Blueprint, render_template, request
from blog.main.forms import MemberForm
from blog.models import Post
import json
import requests

main = Blueprint("main", __name__)


def send_to_google(values):
    url = "https://script.google.com/macros/s/AKfycbza4Lx4a1AO9Ea48C57OoqTGYq2Asqf0ipYG0R5-N8cLj2Fwpc/exec"
    params = {"variables": values}
    requests.post(url, params=params)


@main.route("/")
def index():
    form = MemberForm()
    return render_template("index.html", form=form)


@main.route("/member", methods=["GET", "POST"])
def member():
    form = MemberForm()
    if request.method == "POST" and form.validate_on_submit():
        values = {
            "firstname": form.firstname.data,
            "lastname": form.lastname.data,
            "email": form.email.data,
            "phone": form.phone.data,
            "usn": form.usn.data,
            "branch": form.branch.data,
            "semester": form.semester.data,
        }
        send_to_google(values)
        return render_template("member.html", form=form)
        # flash(
        #     " Dear {}, your registration was successful!".format(
        #         form.firstname.data + form.lastname.data
        #     ),
        #     "success",
        # )
    return render_template("member.html", form=form)


@main.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)


@main.route("/about")
def about():
    return render_template("about.html")
