from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import author_service
from mydb.auth.service.general_service import GeneralService


class AuthorController(GeneralController):
    _service = author_service

    def get_all_songs_by_author(self, id):
        return [song.put_into_dto() for song in self._service.get_all_songs_by_author(id)]

    def get_all_albums_by_author(self, id):
        return [song.put_into_dto() for song in self._service.get_all_albums_by_author(id)]
