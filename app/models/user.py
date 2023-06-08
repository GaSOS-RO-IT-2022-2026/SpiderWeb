from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    email = db.Column(db.String())
    displayname = db.Column(db.String())
    permissions = db.Column(db.Integer)

    def __init__(self, username, password, email, displayname, permissions):
        self.username = username
        self.password = password
        self.email = email
        self.displayname = displayname
        self.permissions = permissions

    def push_to_db(self):
        db.session.add(self)
        db.session.commit()
