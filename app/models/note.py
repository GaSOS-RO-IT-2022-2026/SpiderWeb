from app import db
from datetime import date
from sqlalchemy.dialects.postgresql import ARRAY


class Note(db.Model):
    __tablename__ = "notes"

    noteid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("users.userid"), nullable=False)
    subjectid = db.Column(db.Integer, db.ForeignKey("subjects.subjectid"), nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, default=False)
    attachments = db.Column(ARRAY(db.String))
    created = db.Column(db.Date, nullable=False)

    def __init__(
        self,
        author_id: int,
        subject_id: int,
        title: str,
        content: str,
        attachments: list[str],
        created: date,
    ):
        self.author_id = author_id
        self.subject_id = subject_id
        self.title = title
        self.content = content
        self.attachments = attachments
        self.created = created

    def push_to_db(self):
        db.session.add(self)
        db.session.commit()
