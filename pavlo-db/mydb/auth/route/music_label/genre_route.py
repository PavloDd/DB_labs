from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import genre_controller
from mydb.auth.domain.music_label.genre import Genre

genre_bp = Blueprint("genres", __name__, url_prefix="/genres/")


@genre_bp.get("")
def get_all_genres() -> Response:
    return make_response(jsonify(genre_controller.find_all()), HTTPStatus.OK)


@genre_bp.get("/<int:genre_id>")
def get_genres(genre_id: int) -> Response:
    return make_response(jsonify(genre_controller.find_by_id(genre_id)), HTTPStatus.OK)


@genre_bp.put("/<int:genre_id>")
def update_genre(genre_id: int) -> Response:
    content = request.get_json()
    genre = Genre.create_from_dto(content)
    genre_controller.update(genre_id, genre)
    return make_response("Genre updated", HTTPStatus.OK)


@genre_bp.patch("/<int:genre_id>")
def patch_genre(genre_id: int) -> Response:
    content = request.get_json()
    genre_controller.patch(genre_id, content)
    return make_response("Genre updated", HTTPStatus.OK)


@genre_bp.delete("/<int:genre_id>")
def delete_genre(genre_id: int) -> Response:
    genre_controller.delete(genre_id)
    return make_response("Genre deleted", HTTPStatus.OK)


@genre_bp.post("")
def create_genre() -> Response:
    content = request.get_json()
    genre = Genre.create_from_dto(content)
    genre_id = genre_controller.create(genre)
    return make_response(f"Genre created with ID: {genre_id}", HTTPStatus.CREATED)


@genre_bp.get("/songs/<int:id>")
def get_all_songs_with_genre(id: int):
    return genre_controller.get_all_songs_with_genre(id)
