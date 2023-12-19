from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.music_label.genre import Genre


class GenreDao(GeneralDAO):
    _domain_type = Genre
