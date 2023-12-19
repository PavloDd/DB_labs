from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.music_label.song import Song


class SongDao(GeneralDAO):
    _domain_type = Song
