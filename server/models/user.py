from config import db, bcrypt
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String,
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String,
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String,
        nullable=False
    )
    notes = db.relationship(
        "Note",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    @property
    def password(self):
        raise AttributeError(
            "Password is not readable"
        )

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

    def authenticate(self, password):

        return bcrypt.check_password_hash(
            self.password_hash,
            password
        )