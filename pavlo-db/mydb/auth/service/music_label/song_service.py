from mydb.auth.dao import song_dao
from mydb.auth.service.general_service import GeneralService


class SongService(GeneralService):
    _dao = song_dao

    def get_all_songs_by_author(self):
        ...

