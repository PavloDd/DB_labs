from http import HTTPStatus

from flask import abort

from mydb.auth.dao import author_dao
from mydb.auth.service.general_service import GeneralService


class AuthorService(GeneralService):
    _dao = author_dao

    def get_all_songs_by_author(self, id):
        author = self._dao.find_by_id(id)
        if author is None:
            abort(HTTPStatus.NOT_FOUND)
        return author.songs

    def get_all_albums_by_author(self, id):
        author = self._dao.find_by_id(id)
        if author is None:
            abort(HTTPStatus.NOT_FOUND)
        return author.albums
