from http import HTTPStatus

from flask import abort

from mydb.auth.dao import album_dao
from mydb.auth.service.general_service import GeneralService


class AlbumService(GeneralService):
    _dao = album_dao

    def get_songs_from_album(self, id):
        album = self._dao.find_by_id(id)
        if album is None:
            abort(HTTPStatus.NOT_FOUND)
        return album.songs
