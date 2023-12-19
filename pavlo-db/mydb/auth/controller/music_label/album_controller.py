from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import album_service


class AlbumController(GeneralController):
    _service = album_service

    def get_songs_from_album(self, id):
        return [song.put_into_dto() for song in self._service.get_songs_from_album(id)]
