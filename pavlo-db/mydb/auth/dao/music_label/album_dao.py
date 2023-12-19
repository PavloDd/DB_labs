from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.music_label.album import Album


class AlbumDao(GeneralDAO):
    _domain_type = Album
