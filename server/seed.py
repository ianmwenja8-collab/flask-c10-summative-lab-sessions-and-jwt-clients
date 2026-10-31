from app import app
from config import db
from models.user import User
from models.note import Note
with app.app_context():

    db.drop_all()
    db.create_all()

    user = User(
        username="ian",
        email="ian@gmail.com"
    )

    user.password = "password123"
    db.session.add(user)
    db.session.commit()
    for i in range(10):

        note = Note(
            title=f"Note {i}",
            content="Sample content",
            category="School",
            user_id=user.id
        )

        db.session.add(note)

    db.session.commit()
