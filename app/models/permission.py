from app import db


class Perm(db.Model):
    __tablename__ = "perms"

    permid = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer)
    action = db.Column(db.String())
    resource = db.Column(db.String())

    def __init__(self, weight, action, resource):
        self.weight = weight
        self.action = action
        self.resource = resource

    def push_to_db(self):
        db.session.add(self)
        db.session.commit()
