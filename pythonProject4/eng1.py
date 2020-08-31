from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/atom'
db = SQLAlchemy(app)


class Contactus(db.Model):
    s_no = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(20), nullable=False)


@app.route('/')
def home():
    return render_template('Slidebar.html')


@app.route('/contact.1', methods=['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contactus(name=name, email=email, phone=phone, msg=message)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.1.html')


@app.route('/analog')
def clo():
    return render_template('analog.html')
@app.route('/')
def car():
    return render_template('index.html')

app.run(debug=True)
