from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.music_label.song_has_playlists import SongPlaylistAssociation


class SongPlaylistAssociationDao(GeneralDAO):
    _domain_type = SongPlaylistAssociation
