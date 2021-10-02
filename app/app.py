from flask import Flask,render_template,request,redirect,url_for
from flask import LoginManager,login_user,logout_user,login_required
from hashlib import sha256
from app import key

app = Flask(__name__)

from app.models import db,Content,User
login_manager = LoginManager()
login_manager.init_app(app)
app.config["SECRET_KEY"] = key.SECRET.KEY

@login_manager.user_loader
def load_user(id):
	return User.query.filter_by(id=id).first()

@app.route("/")
def index():
	contents = Content.query.join(User).all()
	return render_template("index.html",contents=contents)


@app.route("/content/<content_id>")
def content(content_id):
	content = Content.query.filter_by(id=content_id).join(User).all()[0]
	return render_template("content.html", content=content)


@app.route("/login")
def login():
	return render_template("login.html")


@app.route("/login_submit",methods=["POST"])
def login_submit():
	


if __name__ == "__main__":
	app.run(debug=True)