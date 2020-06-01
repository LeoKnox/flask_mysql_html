from application import app, mydb
from flask import render_template

mycursor = mydb.cursor()

@app.route("/")
@app.route("/index")
def index():
    mycursor.execute("ALTER TABLE flaskhtmldb ADD COLUMN char_id INT")
    #mycursor.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)
    return render_template("index.html", nav_index="active")