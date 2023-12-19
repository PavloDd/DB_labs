from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import song_has_playlist_service
from mydb.auth.service.general_service import GeneralService


class SongPlaylistAssociationController(GeneralController):
    _service = song_has_playlist_service

    def playlist_song(self):
        return [obj for obj in self._service.playlist_song()]

    def song_playlist(self):
        return [obj for obj in self._service.song_playlist()]
