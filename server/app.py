from flask import Flask
from flask_restful import Api
from flask_jwt_extended import (
    JWTManager
)
from config import db, migrate, bcrypt

from resources.auth import (
    Register,
    Login
)

from resources.notes import (
    NoteList,
    NoteById
)
app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:///app.db"

app.config[
    "JWT_SECRET_KEY"
] = "super-secret-key"

api = Api(app)
db.init_app(app)

migrate.init_app(
    app,
    db
)

bcrypt.init_app(app)

jwt = JWTManager(app)
api.add_resource(
    Register,
    "/register"
)
api.add_resource(
    Login,
    "/login"
)
api.add_resource(
    NoteList,
    "/notes"
)
api.add_resource(
    NoteById,
    "/notes/<int:id>"
)
if __name__ == "__main__":
    app.run(
        port=5555,
        debug=True
    )