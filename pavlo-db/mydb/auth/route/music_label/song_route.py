from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import song_controller
from mydb.auth.domain.music_label.song import Song

song_bp = Blueprint("songs", __name__, url_prefix="/songs/")


@song_bp.get("")
def get_all_songs() -> Response:
    return make_response(jsonify(song_controller.find_all()), HTTPStatus.OK)


@song_bp.get("/<int:song_id>")
def get_songs(song_id: int) -> Response:
    return make_response(jsonify(song_controller.find_by_id(song_id)), HTTPStatus.OK)


@song_bp.put("/<int:song_id>")
def update_song(song_id: int) -> Response:
    content = request.get_json()
    song = Song.create_from_dto(content)
    song_controller.update(song_id, song)
    return make_response("Song updated", HTTPStatus.OK)


@song_bp.patch("/<int:song_id>")
def patch_song(song_id: int) -> Response:
    content = request.get_json()
    song_controller.patch(song_id, content)
    return make_response("Song updated", HTTPStatus.OK)


@song_bp.delete("/<int:song_id>")
def delete_song(song_id: int) -> Response:
    song_controller.delete(song_id)
    return make_response("Song deleted", HTTPStatus.OK)


@song_bp.post("")
def create_song() -> Response:
    content = request.get_json()
    song = Song.create_from_dto(content)
    song_id = song_controller.create(song)
    return make_response(f"Song created with ID: {song_id}", HTTPStatus.CREATED)
