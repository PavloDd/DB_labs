from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import playlist_has_user_controller
from mydb.auth.domain.music_label.playlist_has_user import PlaylistUserAssociation

playlist_has_user_bp = Blueprint(
    "playlist_has_users", __name__, url_prefix="/playlist_has_users/"
)


@playlist_has_user_bp.get("")
def get_all_playlist_has_users() -> Response:
    return make_response(
        jsonify(playlist_has_user_controller.find_all()), HTTPStatus.OK
    )


@playlist_has_user_bp.get("/<int:playlist_has_user_id>")
def get_playlist_has_users(playlist_has_user_id: int) -> Response:
    return make_response(
        jsonify(playlist_has_user_controller.find_by_id(playlist_has_user_id)),
        HTTPStatus.OK,
    )


@playlist_has_user_bp.put("/<int:playlist_has_user_id>")
def update_playlist_has_user(playlist_has_user_id: int) -> Response:
    content = request.get_json()
    playlist_has_user = PlaylistUserAssociation.create_from_dto(content)
    playlist_has_user_controller.update(playlist_has_user_id, playlist_has_user)
    return make_response("PlaylistUserAssociation updated", HTTPStatus.OK)


@playlist_has_user_bp.patch("/<int:playlist_has_user_id>")
def patch_playlist_has_user(playlist_has_user_id: int) -> Response:
    content = request.get_json()
    playlist_has_user_controller.patch(playlist_has_user_id, content)
    return make_response("PlaylistUserAssociation updated", HTTPStatus.OK)


@playlist_has_user_bp.delete("/<int:playlist_has_user_id>")
def delete_playlist_has_user(playlist_has_user_id: int) -> Response:
    playlist_has_user_controller.delete(playlist_has_user_id)
    return make_response("PlaylistUserAssociation deleted", HTTPStatus.OK)


@playlist_has_user_bp.post("")
def create_playlist_has_user() -> Response:
    content = request.get_json()
    playlist_has_user = PlaylistUserAssociation.create_from_dto(content)
    playlist_has_user_id = playlist_has_user_controller.create(playlist_has_user)
    return make_response(
        f"PlaylistUserAssociation created with ID: {playlist_has_user_id}",
        HTTPStatus.CREATED,
    )


@playlist_has_user_bp.get("/playlist_user")
def playlist_user():
    return playlist_has_user_controller.playlist_user()


@playlist_has_user_bp.get("/user_playlist")
def user_playlist():
    return playlist_has_user_controller.user_playlist()
