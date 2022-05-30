from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "29b88f280b5ab6fbc8996226930c6e0b" # secrets.token_hex(16)

posts = [
    {
        "author": "Guillermo N",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "May 29, 2022",
    },
    {
        "author": "Tulio Fra",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "May 30, 2022",
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="LogIn", form=form)

if __name__ == '__main__':
    app.run(debug=True)