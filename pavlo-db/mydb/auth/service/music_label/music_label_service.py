from http import HTTPStatus

from flask import abort

from mydb.auth.dao import music_label_dao
from mydb.auth.service.general_service import GeneralService


class MusicLabelService(GeneralService):
    _dao = music_label_dao

    def get_all_artist(self, id):
        music_label = self._dao.find_by_id(id)
        if not music_label:
            abort(HTTPStatus.NOT_FOUND)
        return music_label.authors
