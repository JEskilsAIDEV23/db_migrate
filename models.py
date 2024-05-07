from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, DateTime, Column, Integer, \
                    String, ForeignKey
db = SQLAlchemy()

#___DB MODEL DEFINITION___#

class AIDev23(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)