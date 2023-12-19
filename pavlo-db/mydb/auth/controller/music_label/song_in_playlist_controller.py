from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import song_in_playlist_service
from mydb.auth.service.general_service import GeneralService


class SongInPlaylistController(GeneralController):
    _service = song_in_playlist_service
