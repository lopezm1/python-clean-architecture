from core.interfaces.person_interface import PersonInterface
from core.entities.professor import Professor
from datetime import datetime, timedelta

future_date = datetime.now() + timedelta(days=1)

class ProfessorRepository(PersonInterface):

    def __init__(self):
        super().__init__()

    # In-Memory Data
    _professor = Professor("Miguel", "Lopez", [], [])

    def get_by_id(self, personal_id):
        return self._professor

    def save(self, person):
        self._professor = person

if __name__ == "__main__":
    repo = ProfessorRepository()

    result = repo.get_by_id("123456")

    print(type(result))
    print(result.first_name)