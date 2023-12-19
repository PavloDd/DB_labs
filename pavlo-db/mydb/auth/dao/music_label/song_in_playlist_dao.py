from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.music_label.song_in_playlist import SongInPlaylist


class SongInPlaylistDao(GeneralDAO):
    _domain_type = SongInPlaylist
