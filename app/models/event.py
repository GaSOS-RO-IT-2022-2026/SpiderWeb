from app import db
from datetime import date
from ..lib.types import EventType


class Event(db.Model):
    __tablename__ = "events"

    eventid = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.Enum(EventType))
    userid = db.Column(db.Integer, db.ForeignKey("users.userid"), nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, default=False)
    deadline = db.Column(db.Date, nullable=True)
    created = db.Column(db.Date, nullable=False)

    def __init__(
        self,
        kind: EventType,
        author_id: int,
        title: str,
        description: str,
        deadline: date,
        created: date,
    ):
        self.kind = kind
        self.author_id = author_id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.created = created

    def push_to_db(self):
        db.session.add(self)
        db.session.commit()
