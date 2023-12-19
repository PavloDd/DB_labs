from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import genre_service
from mydb.auth.service.general_service import GeneralService


class GenreController(GeneralController):
    _service = genre_service

    def get_all_songs_with_genre(self, id):
        return [song.put_into_dto() for song in self._service.get_all_songs_with_genre(id)]
