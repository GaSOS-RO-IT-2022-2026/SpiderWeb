from app import db


class Subject(db.Model):
    __tablename__ = "subjects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    teacher = db.Column(db.String())

    def __init__(self, name: str, teacher: str):
        self.name = name
        self.teacher = teacher

    def push_to_db(self):
        db.session.add(self)
        db.session.commit()
