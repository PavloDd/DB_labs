from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import user_has_song_service


class UserSongAssociationController(GeneralController):
    _service = user_has_song_service

    def user_song(self):
        return [obj for obj in self._service.user_song()]

    def song_user(self):
        return [obj for obj in self._service.song_user()]
