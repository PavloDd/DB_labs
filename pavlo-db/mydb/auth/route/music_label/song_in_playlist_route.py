from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import song_in_playlist_controller
from mydb.auth.domain.music_label.song_in_playlist import SongInPlaylist

song_in_playlist_bp = Blueprint(
    "song_in_playlists", __name__, url_prefix="/song_in_playlists/"
)


@song_in_playlist_bp.get("")
def get_all_song_in_playlists() -> Response:
    return make_response(jsonify(song_in_playlist_controller.find_all()), HTTPStatus.OK)


@song_in_playlist_bp.get("/<int:song_in_playlist_id>")
def get_song_in_playlists(song_in_playlist_id: int) -> Response:
    return make_response(
        jsonify(song_in_playlist_controller.find_by_id(song_in_playlist_id)),
        HTTPStatus.OK,
    )


@song_in_playlist_bp.put("/<int:song_in_playlist_id>")
def update_song_in_playlist(song_in_playlist_id: int) -> Response:
    content = request.get_json()
    song_in_playlist = SongInPlaylist.create_from_dto(content)
    song_in_playlist_controller.update(song_in_playlist_id, song_in_playlist)
    return make_response("SongInPlaylist updated", HTTPStatus.OK)


@song_in_playlist_bp.patch("/<int:song_in_playlist_id>")
def patch_song_in_playlist(song_in_playlist_id: int) -> Response:
    content = request.get_json()
    song_in_playlist_controller.patch(song_in_playlist_id, content)
    return make_response("SongInPlaylist updated", HTTPStatus.OK)


@song_in_playlist_bp.delete("/<int:song_in_playlist_id>")
def delete_song_in_playlist(song_in_playlist_id: int) -> Response:
    song_in_playlist_controller.delete(song_in_playlist_id)
    return make_response("SongInPlaylist deleted", HTTPStatus.OK)


@song_in_playlist_bp.post("")
def create_song_in_playlist() -> Response:
    content = request.get_json()
    song_in_playlist = SongInPlaylist.create_from_dto(content)
    song_in_playlist_id = song_in_playlist_controller.create(song_in_playlist)
    return make_response(
        f"SongInPlaylist created with ID: {song_in_playlist_id}", HTTPStatus.CREATED
    )
