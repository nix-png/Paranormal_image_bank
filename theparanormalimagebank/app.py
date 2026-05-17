import base64
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Custom filter
@app.template_filter('b64encode')
def b64encode_filter(data):
    return base64.b64encode(data).decode('utf-8')

app.jinja_env.filters['b64encode'] = b64encode_filter

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///images.db")



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/",methods=["GET", "POST"])
@login_required
def index():
    """Show images and translations"""
    if request.method == "POST":
        a = "%"
        search = request.form.get("search")
        searchgood = a + search + a
        if search:
            if request.form.get("searchby") == 'name':
                images = db.execute("SELECT * FROM images WHERE name like ? ",searchgood)
                return render_template("index.html", images=images)

            elif request.form.get("searchby") != 'name':
                images = db.execute("SELECT * FROM images WHERE translation like ? ",searchgood)
                return render_template("index.html", images=images)


    images = db.execute("SELECT * FROM images")
    return render_template("index.html", images=images)


@app.route("/update_translation", methods=["POST"])
@login_required
def update_translation():
    data = request.get_json()
    id = data['id']
    new_translation = data['translation']
    db.execute("UPDATE images SET translation = ? WHERE id = ?", new_translation, id)
    return '', 204

@app.route("/add_image", methods=["GET", "POST"])
@login_required
def add_image():

    """Add image to the database"""
    if request.method == "POST":
        text = request.form.get("text")
        name = request.form.get("name")
        if 'file' not in request.files:
            return apology("No file part", 400)

        file = request.files['file']

        if file.filename == '':
            return apology("No selected file", 400)

        if file:
            binary_data = file.read()
            db.execute("INSERT INTO images (name,translation, images) VALUES (?, ?,?)",name, text, binary_data)
            return redirect("/")

    return render_template("add_image.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 403)


        # Ensure username exists and password is correct
        if request.form.get("password") != "MapleMaypole":
            return apology("invalid password", 403)

        # Remember which user has logged in
        session["user_id"] = 1

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



