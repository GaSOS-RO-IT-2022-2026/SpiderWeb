from app import db

class ExampleModel(db.Model):
    __tablename__ = 'example'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name
    
    def push_to_db(self):
        db.session.add(self)
        db.session.commit()
