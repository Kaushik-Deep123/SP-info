from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/spinfosys"
db = SQLAlchemy(app)


class Contacts(db.Model):
    """sno, name, email, subject, Message"""
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(12), unique=True, nullable=False)
    subject = db.Column(db.String(120), unique=True, nullable=False)
    Message = db.Column(db.String(120), unique=True, nullable=False)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/account")
def account_details():
    return render_template('account.html')

@app.route("/ab")
def about_section():
    return render_template('about.html')

@app.route("/server")
def server_section():
    return render_template('server.html')

@app.route("/audit")
def audit_section():
    return render_template('audit.html')

@app.route("/amc")
def amc_section():
    return render_template('AMC.html')

@app.route("/lap")
def lap_section():
    return render_template('laptop.html')

@app.route("/desk")
def desk_section():
    return render_template('desktop.html')

@app.route("/print")
def print_section():
    return render_template('printer.html')

@app.route("/tes")
def testimoni_section():
    return render_template('testimoni.html')

@app.route("/contact", methods = ['GET', 'POST'])
def contact_section():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        """sno, name, email, subject, Message"""

        entry = Contacts(name = name, email = email, subject = subject, Message = message)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')
    

app.run(debug=True)