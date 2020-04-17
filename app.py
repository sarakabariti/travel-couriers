from flask import Flask, render_template, url_for, request, redirect, session

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['secret_key'] = "secretkey"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\DELL\\Documents\\foundations\\travel-couriers\\database.db'
db = SQLAlchemy(app)  

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)


class contact_us(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(1000), nullable=False)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        subject = request.form["subject"]

        contact = contact_us(firstname=firstname,
                             lastname=lastname,
                             email=email,
                             subject=subject)
        db.session.add(contact)
        db.session.commit()

    return render_template("contact.html")


@app.route('/how')
def how():
    return render_template("how.html")

if __name__ == "__main__":
    app.run(debug=True)
