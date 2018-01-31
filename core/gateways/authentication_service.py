from core.interfaces.authentication_interface import AuthenticationInterface

class AuthenticationService(AuthenticationInterface):
    def __init__(self):
        super().__init__()

    def is_logged_in(self):
        return True
