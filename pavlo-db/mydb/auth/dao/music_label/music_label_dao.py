from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.music_label.music_label import MusicLabel


class MusicLabelDao(GeneralDAO):
    _domain_type = MusicLabel
