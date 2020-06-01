from application import app, mydb
from flask import render_template

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

@app.route("/")
@app.route("/index")
def index():
    for x in mycursor:
        print(x)
    return render_template("index.html", nav_index="active")