from http import HTTPStatus

from flask import abort

from mydb.auth.dao import playlist_dao
from mydb.auth.service.general_service import GeneralService


class PlaylistService(GeneralService):
    _dao = playlist_dao

    def get_songs_in_playlist(self, id):
        playlist = self._dao.find_by_id(id)
        if playlist is None:
            abort(HTTPStatus.NOT_FOUND)
        return playlist.songs_in_playlist
