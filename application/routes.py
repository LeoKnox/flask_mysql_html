from application import app, mydb
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    print (mydb)
    return render_template("index.html", nav_index="active")