from abc import abstractmethod
from core.interfaces.bases.base_mysql import BaseMySQL

class CourseInterface(BaseMySQL):

    @abstractmethod
    def get_by_code(self, code):
        pass