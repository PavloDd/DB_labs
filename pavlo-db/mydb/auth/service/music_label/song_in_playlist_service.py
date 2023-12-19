from mydb.auth.dao import song_in_playlist_dao
from mydb.auth.service.general_service import GeneralService


class SongInPlaylistService(GeneralService):
    _dao = song_in_playlist_dao
