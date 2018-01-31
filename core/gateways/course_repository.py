from core.interfaces.course_interface import CourseInterface
from core.entities.course import Course
from datetime import datetime, timedelta

future_date = datetime.now() + timedelta(days=1)

class CourseRepository(CourseInterface):

    def __init__(self):
        super().__init__()
        print(self.conn_str)

    # In-Memory Data
    data = {
        'ASU101': Course('ASU101', 'Introduction to ASU', future_date),
        'CSE110': Course('CSE110', 'Introduction to Programming', future_date),
        'CSE120': Course('CSE120', 'Introduction to Circuits', future_date)
    }

    def get_by_code(self, code):
        return self.data[code]

    def get_all(self):
        return self.data

if __name__ == "__main__":
    repo = CourseRepository()

    result = repo.get_by_code('ASU101')

    print(result.course_code, result.course_name, result.course_start)


