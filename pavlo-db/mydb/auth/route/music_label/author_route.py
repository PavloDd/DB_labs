from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import author_controller
from mydb.auth.domain.music_label.author import Author

author_bp = Blueprint("authors", __name__, url_prefix="/authors/")


@author_bp.get("")
def get_all_authors() -> Response:
    return make_response(jsonify(author_controller.find_all()), HTTPStatus.OK)


@author_bp.get("/<int:author_id>")
def get_authors(author_id: int) -> Response:
    return make_response(
        jsonify(author_controller.find_by_id(author_id)), HTTPStatus.OK
    )


@author_bp.put("/<int:author_id>")
def update_author(author_id: int) -> Response:
    content = request.get_json()
    author = Author.create_from_dto(content)
    author_controller.update(author_id, author)
    return make_response("Author updated", HTTPStatus.OK)


@author_bp.patch("/<int:author_id>")
def patch_author(author_id: int) -> Response:
    content = request.get_json()
    author_controller.patch(author_id, content)
    return make_response("Author updated", HTTPStatus.OK)


@author_bp.delete("/<int:author_id>")
def delete_author(author_id: int) -> Response:
    author_controller.delete(author_id)
    return make_response("Author deleted", HTTPStatus.OK)


@author_bp.post("")
def create_author() -> Response:
    content = request.get_json()
    author = Author.create_from_dto(content)
    author_id = author_controller.create(author)
    return make_response(f"Author created with ID: {author_id}", HTTPStatus.CREATED)


@author_bp.get("/songs/<int:id>")
def get_all_songs_by_author(id: int):
    return author_controller.get_all_songs_by_author(id)


@author_bp.get("/albums/<int:id>")
def get_all_albums_by_author(id: int):
    return author_controller.get_all_albums_by_author(id)
