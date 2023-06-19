from app import db
from datetime import date


class Feed(db.Model):
    __tablename__ = "statuses"

    feedid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("users.userid"), nullable=False)
    message = db.Column(db.String, nullable=False)
    announcement = db.Column(db.Boolean, default=False)
    created = db.Column(db.Date, nullable=False)

    def __init__(
        self, author_id: int, message: str, created: date, announcement: bool = False
    ):
        self.author_id = author_id
        self.message = message
        self.announcement = announcement
        self.created = created

    def push_to_db(self):
        db.session.add(self)
        db.session.commit()
