from abc import abstractmethod
from core.interfaces.bases.base_mysql import BaseMySQL

class PersonInterface(BaseMySQL):

    @abstractmethod
    def get_by_id(self, personal_id):
        pass

    @abstractmethod
    def save(self, person):
        pass