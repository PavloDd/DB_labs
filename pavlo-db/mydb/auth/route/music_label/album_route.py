from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import album_controller
from mydb.auth.domain.music_label.album import Album

album_bp = Blueprint("albums", __name__, url_prefix="/albums/")


@album_bp.get("")
def get_all_albums() -> Response:
    return make_response(jsonify(album_controller.find_all()), HTTPStatus.OK)


@album_bp.get("/<int:album_id>")
def get_albums(album_id: int) -> Response:
    return make_response(jsonify(album_controller.find_by_id(album_id)), HTTPStatus.OK)


@album_bp.put("/<int:album_id>")
def update_album(album_id: int) -> Response:
    content = request.get_json()
    album = Album.create_from_dto(content)
    album_controller.update(album_id, album)
    return make_response("Album updated", HTTPStatus.OK)


@album_bp.patch("/<int:album_id>")
def patch_album(album_id: int) -> Response:
    content = request.get_json()
    album_controller.patch(album_id, content)
    return make_response("Album updated", HTTPStatus.OK)


@album_bp.delete("/<int:album_id>")
def delete_album(album_id: int) -> Response:
    album_controller.delete(album_id)
    return make_response("Album deleted", HTTPStatus.OK)


@album_bp.post("")
def create_album() -> Response:
    content = request.get_json()
    album = Album.create_from_dto(content)
    album_id = album_controller.create(album)
    return make_response(f"Album created with ID: {album_id}", HTTPStatus.CREATED)


@album_bp.get("/songs/<int:id>")
def get_all_songs_with_genre(id: int):
    return album_controller.get_songs_from_album(id)
