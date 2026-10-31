from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)
from config import db
from models.note import Note
class NoteList(Resource):
    @jwt_required()
    def get(self):

        user_id = get_jwt_identity()

        page = request.args.get(
            "page",
            1,
            type=int
        )
        notes = Note.query.filter_by(
            user_id=user_id
        ).paginate(
            page=page,
            per_page=5
        )
        return {
            "page": notes.page,
            "pages": notes.pages,
            "notes": [
                {
                    "id": note.id,
                    "title": note.title,
                    "content": note.content,
                    "category": note.category
                }
                for note in notes.items
            ]
        }, 200
    @jwt_required()
    def post(self):

        user_id = get_jwt_identity()

        data = request.get_json()

        note = Note(
            title=data["title"],
            content=data["content"],
            category=data["category"],
            user_id=user_id
        )

        db.session.add(note)

        db.session.commit()

        return {
            "message": "Note created"
        }, 201

class NoteById(Resource):
    @jwt_required()
    def get(self, id):

        user_id = get_jwt_identity()
        note = Note.query.filter_by(
            id=id,
            user_id=user_id
        ).first()
        if not note:

            return {
                "message": "Not Found"
            }, 404
        return {
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "category": note.category
        }, 200
    @jwt_required()
    def patch(self, id):

        user_id = get_jwt_identity()

        note = Note.query.filter_by(
            id=id,
            user_id=user_id
        ).first()

        if not note:

            return {
                "message": "Not Found"
            }, 404

        data = request.get_json()
        note.title = data.get(
            "title",
            note.title
        )
        note.content = data.get(
            "content",
            note.content
        )
        note.category = data.get(
            "category",
            note.category
        )

        db.session.commit()

        return {
            "message": "Updated"
        }, 200
    @jwt_required()
    def delete(self, id):
        user_id = get_jwt_identity()

        note = Note.query.filter_by(
            id=id,
            user_id=user_id
        ).first()
        if not note:

            return {
                "message": "Not Found"
            }, 404

        db.session.delete(note)
        db.session.commit()
        return {
            "message": "Deleted"
        }, 200