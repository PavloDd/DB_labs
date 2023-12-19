from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import song_has_playlist_controller
from mydb.auth.domain.music_label.song_has_playlists import SongPlaylistAssociation

song_has_playlists_bp = Blueprint(
    "song_has_playlists", __name__, url_prefix="/song_has_playlists/"
)


@song_has_playlists_bp.get("")
def get_all_song_has_playlists() -> Response:
    return make_response(
        jsonify(song_has_playlist_controller.find_all()), HTTPStatus.OK
    )


@song_has_playlists_bp.get("/<int:song_has_playlists_id>")
def get_song_has_playlists(song_has_playlists_id: int) -> Response:
    return make_response(
        jsonify(song_has_playlist_controller.find_by_id(song_has_playlists_id)),
        HTTPStatus.OK,
    )


@song_has_playlists_bp.put("/<int:song_has_playlists_id>")
def update_song_has_playlists(song_has_playlists_id: int) -> Response:
    content = request.get_json()
    song_has_playlists = SongPlaylistAssociation.create_from_dto(content)
    song_has_playlist_controller.update(song_has_playlists_id, song_has_playlists)
    return make_response("SongPlaylistAssociation updated", HTTPStatus.OK)


@song_has_playlists_bp.patch("/<int:song_has_playlists_id>")
def patch_song_has_playlists(song_has_playlists_id: int) -> Response:
    content = request.get_json()
    song_has_playlist_controller.patch(song_has_playlists_id, content)
    return make_response("SongPlaylistAssociation updated", HTTPStatus.OK)


@song_has_playlists_bp.delete("/<int:song_has_playlists_id>")
def delete_song_has_playlists(song_has_playlists_id: int) -> Response:
    song_has_playlist_controller.delete(song_has_playlists_id)
    return make_response("SongPlaylistAssociation deleted", HTTPStatus.OK)


@song_has_playlists_bp.post("")
def create_song_has_playlists() -> Response:
    content = request.get_json()
    song_has_playlists = SongPlaylistAssociation.create_from_dto(content)
    song_has_playlists_id = song_has_playlist_controller.create(song_has_playlists)
    return make_response(
        f"SongPlaylistAssociation created with ID: {song_has_playlists_id}",
        HTTPStatus.CREATED,
    )

@song_has_playlists_bp.get("/playlist_song")
def playlist_user():
    return song_has_playlist_controller.playlist_song()


@song_has_playlists_bp.get("/song_playlist")
def user_playlist():
    return song_has_playlist_controller.song_playlist()
