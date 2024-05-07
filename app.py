from flask import Flask, render_template, redirect, url_for, request
from flask_migrate import Migrate, upgrade
from models import db
import os
from models import AIDev23 #Import Table AIDev23 
from sqlalchemy import update
from sqlalchemy.sql import func

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///aidev23.db"
app.config["SECRET_KEY"] = "AIDEV23S"
app.config["SECURITY_PASSWORD_SALT"] = "aidev23s"
db.init_app(app)
migrate = Migrate(app, db)

def seed_db():
    member_1 = AIDev23(name="Johan")
    member_2 = AIDev23(name="Khaled")
    member_3 = AIDev23(name="Martin")
    member_4 = AIDev23(name="Wille")
    member_5 = AIDev23(name="Amer")
    member_6 = AIDev23(name="Lucas")
    db.session.add(member_1)
    db.session.add(member_2)
    db.session.add(member_3)
    db.session.add(member_4)
    db.session.add(member_5)
    db.session.add(member_6)
    db.session.commit()

def seed_who():
    members = AIDev23.query

    for member in members:
        if member.id == 1:
            n = member.id
            name = member.name
            description = "GreyBeard"
            db.session.delete(member)
            db.session.commit()
            member = AIDev23(id=n, name=name, description=description)
            db.session.add(member)
        if member.id > 1:
            n = member.id
            name = member.name
            description = "Hacker"
            db.session.delete(member)
            db.session.commit()
            member = AIDev23(id=n, name=name, description=description)
            db.session.add(member)
    db.session.commit()


@app.route("/")
def hello_world():
    members = AIDev23.query
    return render_template('index.html', members=members)

@app.route("/who")
def who():
     members = AIDev23.query
     return render_template('who.html', members=members)

if __name__ == '__main__':
    with app.app_context():
        upgrade()
        db.create_all()
        members = AIDev23.query
        if members.count() < 6:
            seed_db()
        # seed_who()

app.run(debug=True, port=4500)