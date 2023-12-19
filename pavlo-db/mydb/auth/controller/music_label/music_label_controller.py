from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import music_label_service


class MusicLabelController(GeneralController):
    _service = music_label_service

    def get_all_artist(self, id):
        return [author.put_into_dto() for author in self._service.get_all_artist(id)]
