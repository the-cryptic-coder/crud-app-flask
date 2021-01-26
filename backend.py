from flask import Flask, redirect, url_for, render_template, request
import sqlite3
import smtplib
app = Flask(__name__)
conn=sqlite3.connect('testing.db')
# Table name is test
c=conn.cursor()
c.execute("SELECT * FROM test")
items= c.fetchall()
for item in items:
    print(item[0]+" "+item[1])



@app.route("/", methods=["POST", "GET"])
def login():
    conn=sqlite3.connect('testing.db')
    # Table name is test
    c=conn.cursor()
    print('calling login()')
    b=False
    if request.method == "POST":
        name = request.form["nm"]
        name2= request.form["lnm"]
        c.execute("SELECT * FROM test")
        items= c.fetchall()
        for item in items:
            if item[0]==name:
                return "<h1>Name already in Database</h1>"
            elif item[0]=='' or item[1]=='':
                return "<h1>Please enter a value</h1>"
        c.execute("INSERT INTO test (first_name,last_name) VALUES (?,?)",(name,name2))
        conn.commit()
        print(name2)
        return render_template("page.html", fname=name, lname=name2)
    else:
        return render_template("front_end.html")

@app.route("/front_end")
def user():
    return render_template("front_end.html")


@app.route("/find_values", methods=["POST", "GET"])
def find():
    print('find()')
    conn=sqlite3.connect('testing.db')
    # Table name is test
    c=conn.cursor()
    print('calling login()')
    b=False
    if request.method == "POST":
        name = request.form["nm"]
        c.execute("SELECT * FROM test")
        items= c.fetchall()
        for item in items:
            if item[0]==name:
                name=item[0]
                name2=item[1]
                b=True
            # else:
            #     return "<h1>Sorry name not in Database</h1>"
        return render_template("page2.html", fname=name, lname=name2)
    else:
        return render_template("find_values.html")

if __name__ == "__main__":
    app.run(debug=True)