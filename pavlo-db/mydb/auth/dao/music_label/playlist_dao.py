from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.music_label.playlist import Playlist


class PlaylistDao(GeneralDAO):
    _domain_type = Playlist
