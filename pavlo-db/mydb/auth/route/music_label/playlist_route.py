from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import playlist_controller
from mydb.auth.domain.music_label.playlist import Playlist

playlist_bp = Blueprint("playlists", __name__, url_prefix="/playlists/")


@playlist_bp.get("")
def get_all_playlists() -> Response:
    return make_response(jsonify(playlist_controller.find_all()), HTTPStatus.OK)


@playlist_bp.get("/<int:playlist_id>")
def get_playlists(playlist_id: int) -> Response:
    return make_response(
        jsonify(playlist_controller.find_by_id(playlist_id)), HTTPStatus.OK
    )


@playlist_bp.put("/<int:playlist_id>")
def update_playlist(playlist_id: int) -> Response:
    content = request.get_json()
    playlist = Playlist.create_from_dto(content)
    playlist_controller.update(playlist_id, playlist)
    return make_response("Playlist updated", HTTPStatus.OK)


@playlist_bp.patch("/<int:playlist_id>")
def patch_playlist(playlist_id: int) -> Response:
    content = request.get_json()
    playlist_controller.patch(playlist_id, content)
    return make_response("Playlist updated", HTTPStatus.OK)


@playlist_bp.delete("/<int:playlist_id>")
def delete_playlist(playlist_id: int) -> Response:
    playlist_controller.delete(playlist_id)
    return make_response("Playlist deleted", HTTPStatus.OK)


@playlist_bp.post("")
def create_playlist() -> Response:
    content = request.get_json()
    playlist = Playlist.create_from_dto(content)
    playlist_id = playlist_controller.create(playlist)
    return make_response(f"Playlist created with ID: {playlist_id}", HTTPStatus.CREATED)


@playlist_bp.get("/playlist/<int:id>")
def get_songs_in_playlist(id: int):
    print(playlist_controller.get_songs_in_playlist(id))
    return playlist_controller.get_songs_in_playlist(id)
