from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import user_service
from mydb.auth.service.general_service import GeneralService


class UserController(GeneralController):
    _service = user_service
