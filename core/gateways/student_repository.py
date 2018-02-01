from core.interfaces.person_interface import PersonInterface
from core.entities.student import Student
from datetime import datetime, timedelta

future_date = datetime.now() + timedelta(days=1)

class StudentRepository(PersonInterface):

    def __init__(self):
        super().__init__()

    # In-Memory Data
    _student = Student("Miguel", "Lopez", [], [])

    def get_by_id(self, personal_id):
        return self._student

    def save(self, person):
        self._student = person