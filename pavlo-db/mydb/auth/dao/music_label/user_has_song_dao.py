from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.music_label.user_has_song import UserSongAssociation


class UserSongAssociationDao(GeneralDAO):
    _domain_type = UserSongAssociation
