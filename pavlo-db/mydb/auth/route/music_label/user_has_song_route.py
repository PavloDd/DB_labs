from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import user_has_song_controller
from mydb.auth.domain.music_label.user_has_song import UserSongAssociation

user_has_song_bp = Blueprint("user_has_songs", __name__, url_prefix="/user_has_songs/")


@user_has_song_bp.get("")
def get_all_user_has_songs() -> Response:
    return make_response(jsonify(user_has_song_controller.find_all()), HTTPStatus.OK)


@user_has_song_bp.get("/<int:user_has_song_id>")
def get_user_has_songs(user_has_song_id: int) -> Response:
    return make_response(
        jsonify(user_has_song_controller.find_by_id(user_has_song_id)), HTTPStatus.OK
    )


@user_has_song_bp.put("/<int:user_has_song_id>")
def update_user_has_song(user_has_song_id: int) -> Response:
    content = request.get_json()
    user_has_song = UserSongAssociation.create_from_dto(content)
    user_has_song_controller.update(user_has_song_id, user_has_song)
    return make_response("UserSongAssociation updated", HTTPStatus.OK)


@user_has_song_bp.patch("/<int:user_has_song_id>")
def patch_user_has_song(user_has_song_id: int) -> Response:
    content = request.get_json()
    user_has_song_controller.patch(user_has_song_id, content)
    return make_response("UserSongAssociation updated", HTTPStatus.OK)


@user_has_song_bp.delete("/<int:user_has_song_id>")
def delete_user_has_song(user_has_song_id: int) -> Response:
    user_has_song_controller.delete(user_has_song_id)
    return make_response("UserSongAssociation deleted", HTTPStatus.OK)


@user_has_song_bp.post("")
def create_user_has_song() -> Response:
    content = request.get_json()
    user_has_song = UserSongAssociation.create_from_dto(content)
    user_has_song_id = user_has_song_controller.create(user_has_song)
    return make_response(
        f"UserSongAssociation created with ID: {user_has_song_id}", HTTPStatus.CREATED
    )


@user_has_song_bp.get("/user_song")
def user_song():
    return user_has_song_controller.user_song()


@user_has_song_bp.get("/song_user")
def song_user():
    return user_has_song_controller.song_user()
