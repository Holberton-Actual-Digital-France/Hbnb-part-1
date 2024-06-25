# create_database.py
from yourapp import db, app

with app.app_context():
    db.create_all()
