from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import playlist_service
from mydb.auth.service.general_service import GeneralService


class PlaylistController(GeneralController):
    _service = playlist_service

    def get_songs_in_playlist(self, id):
        return [obj.put_into_dto() for obj in self._service.get_songs_in_playlist(id)]
