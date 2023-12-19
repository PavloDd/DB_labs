from http import HTTPStatus

from flask import abort

from mydb.auth.dao import genre_dao
from mydb.auth.service.general_service import GeneralService


class GenreService(GeneralService):
    _dao = genre_dao

    def get_all_songs_with_genre(self, id):
        genre = self._dao.find_by_id(id)
        if genre is None:
            abort(HTTPStatus.NOT_FOUND)
        return genre.songs

