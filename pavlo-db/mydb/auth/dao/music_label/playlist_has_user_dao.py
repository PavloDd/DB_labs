from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.music_label.playlist_has_user import PlaylistUserAssociation


class PlaylistUserAssociationDao(GeneralDAO):
    _domain_type = PlaylistUserAssociation
