from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import music_label_controller
from mydb.auth.domain.music_label.music_label import MusicLabel

music_label_bp = Blueprint("music_labels", __name__, url_prefix="/music_labels/")


@music_label_bp.get("")
def get_all_music_labels() -> Response:
    return make_response(jsonify(music_label_controller.find_all()), HTTPStatus.OK)


@music_label_bp.get("/<int:music_label_id>")
def get_music_labels(music_label_id: int) -> Response:
    return make_response(
        jsonify(music_label_controller.find_by_id(music_label_id)), HTTPStatus.OK
    )


@music_label_bp.put("/<int:music_label_id>")
def update_music_label(music_label_id: int) -> Response:
    content = request.get_json()
    music_label = MusicLabel.create_from_dto(content)
    music_label_controller.update(music_label_id, music_label)
    return make_response("MusicLabel updated", HTTPStatus.OK)


@music_label_bp.patch("/<int:music_label_id>")
def patch_music_label(music_label_id: int) -> Response:
    content = request.get_json()
    music_label_controller.patch(music_label_id, content)
    return make_response("MusicLabel updated", HTTPStatus.OK)


@music_label_bp.delete("/<int:music_label_id>")
def delete_music_label(music_label_id: int) -> Response:
    music_label_controller.delete(music_label_id)
    return make_response("MusicLabel deleted", HTTPStatus.OK)


@music_label_bp.post("")
def create_music_label() -> Response:
    content = request.get_json()
    music_label = MusicLabel.create_from_dto(content)
    music_label_id = music_label_controller.create(music_label)
    return make_response(
        f"MusicLabel created with ID: {music_label_id}", HTTPStatus.CREATED
    )


@music_label_bp.get("/artists/<int:id>")
def get_all_artist(id):
    return music_label_controller.get_all_artist(id)
