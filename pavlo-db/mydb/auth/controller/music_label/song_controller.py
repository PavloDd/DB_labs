from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import song_service
from mydb.auth.service.general_service import GeneralService


class SongController(GeneralController):
    _service = song_service
