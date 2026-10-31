from config import db
class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String,
        nullable=False
    )
    content = db.Column(
        db.Text,
        nullable=False
    )
    category = db.Column(
        db.String
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id"
        )
    )
    user = db.relationship(
        "User",
        back_populates="notes"
    )