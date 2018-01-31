from core.common.entity_model import EntityModel
from datetime import datetime

class Course(EntityModel):

    def __init__(self, course_code: str, course_name: str, course_start: datetime):
        self.course_code = course_code
        self.course_name = course_name
        self.course_start = course_start

    @classmethod
    def from_dict(cls, adict):
        return cls(adict['course_code'],
                   adict['course_name'],
                   adict['course_start'])

if __name__ == "__main__":

    obj = {
        'course_code': 'ASU101',
        'course_name': 'Introduction to ASU',
        'course_start': '2012-08-21 12:00:00 PM'
    }

    class1 = Course.from_dict(obj)

    print(class1.course_code)
    print(class1.course_name)
    print(class1.course_start)
