from abc import abstractmethod
from core.interfaces.bases.base_mysql import BaseMySQL

class AuthenticationInterface(BaseMySQL):

    @abstractmethod
    def is_logged_in(self):
        pass
