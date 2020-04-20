from flask import Flask, render_template, url_for, request, redirect, session

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc


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
    if request.method == "POST":
        req = request.form 
        for x in req:
            if x == "firstname":
                _init__ = None
                try:
                    firstname = request.form['firstname']
                    lastname = request.form['lastname']
                    email = request.form['email']
                    password = request.form["password"]

                    register = user(firstname=firstname,
                                    lastname=lastname,
                                    email=email,
                                    password=password)
                    db.session.add(register)
                    db.session.commit()

                    Message = "success"
                    return render_template("requests.html", Message_up=Message)

                except exc.IntegrityError: 
                    db.session.rollback()

                    error_up = "We already have user with same email or password"
                    return render_template("index.html", Message_up=error_up)

            else:
                email = request.form['email']
                password = request.form["password"]

                login = user.query.filter_by(
                    email=email, password=password).first()

                if login is not None:
                    Message_success = "success"
                    return render_template("requests.html", Message=Message_success)

                if login is None:
                    error = "Incorrect combination of password or email"
                    return render_template("index.html", Message=error)

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
        return render_template("contact-form_success.html")

    return render_template("contact.html")


@app.route('/how')
def how():
    return render_template("how.html")

@app.route('/requests')
def requests():
    return render_template("requests.html")

if __name__ == "__main__":
    app.run(debug=True)
