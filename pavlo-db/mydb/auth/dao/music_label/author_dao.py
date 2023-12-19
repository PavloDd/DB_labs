from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.music_label.author import Author


class AuthorDao(GeneralDAO):
    _domain_type = Author
