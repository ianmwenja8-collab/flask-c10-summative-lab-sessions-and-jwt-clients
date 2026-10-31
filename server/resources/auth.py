from flask import request
from flask_restful import Resource

from flask_jwt_extended import (
    create_access_token
)
from config import db
from models.user import User

class Register(Resource):

    def post(self):

        data = request.get_json()

        user = User(
            username=data["username"],
        
        )

        user.password = data["password"]

        db.session.add(user)

        db.session.commit()

        return {
            "message": "User created"
        }, 201

class Login(Resource):

    def post(self):

        data = request.get_json()

        user = User.query.filter_by(
            username=data["username"]
        ).first()

        if user and user.authenticate(
            data["password"]
        ):

            token = create_access_token(
    identity=str(user.id)
)

            return {
                "token": token
            }, 200
        return {
            "message":
            "Invalid username or password"
        }, 401