from abc import abstractmethod
from core.repositories.bases.base_mysql import BaseMySQL

class NotificationInterface(BaseMySQL):

    @abstractmethod
    def is_logged_in(self):
        pass
