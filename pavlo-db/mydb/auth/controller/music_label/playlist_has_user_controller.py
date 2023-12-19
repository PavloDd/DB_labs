from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import playlist_has_user_service


class PlaylistUserAssociationController(GeneralController):
    _service = playlist_has_user_service

    def playlist_user(self):
        return [obj for obj in self._service.playlist_user()]

    def user_playlist(self):
        return [obj for obj in self._service.user_playlist()]
