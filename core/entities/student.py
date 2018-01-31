from datetime import datetime
from typing import List

from core.common.entity_model import EntityModel
from core.entities.course import Course

CourseList = List[Course]

class Student(EntityModel):

    def __init__(self, first_name: str, last_name: str,
                 registered_courses: CourseList,
                 enrolled_courses: CourseList):
        self.first_name = first_name
        self.last_name = last_name
        self.registered_courses = registered_courses[:]
        self.enrolled_courses = enrolled_courses[:]

    @classmethod
    def from_dict(cls, adict):
        return cls(adict['first_name'],
                   adict['last_name'],
                   adict['registered_courses'][:],
                   adict['enrolled_courses'][:])

    def register_for_course(self, course: Course):

        # Student has not previously enrolled
        if(any(x.course_code in course.course_code for x in self.enrolled_courses)):
            return False

        # Cannot register after class start date
        if(datetime.now() > course.course_start):
            return False

        self.registered_courses.append(course)
        return True



if __name__ == "__main__":

    old_date = datetime.strptime('2012-08-21', '%Y-%m-%d')
    new_date = datetime.strptime('2022-08-21', '%Y-%m-%d')
    obj = {
        'first_name': 'miguel',
        'last_name': 'lopez',
        'registered_courses': [
            Course('ASU101','Introduction to ASU', old_date),
            Course('CSE100','Introduction to Java', old_date),
            Course('CSE150','Fake Engineerings', old_date),
        ],
        'enrolled_courses': [
            Course('CSE110','Circuits', old_date),
            Course('CSE255','Data Structures and Algorithms', old_date),
            Course('ART410','Advanced Art', old_date),
        ]
    }

    double_enroll = Course('CSE110','Circuits', new_date)
    new_enroll = Course('CSE360', 'Intro to Software Engineering', new_date)
    old_enroll = Course('CSE120', 'Logic Boards', old_date)
    stu1 = Student.from_dict(obj)

    # Print List
    print(*stu1.registered_courses, sep=', ')
    # Prints false bc course has been previously enrolled
    print(stu1.register_for_course(double_enroll))

    # Prints false bc course has already passed enrollment date
    print(stu1.register_for_course(old_enroll))
    # Prints true bc course has not been enrolled
    print(stu1.register_for_course(new_enroll))

    # Still compiles but PyCharm IDE will show you type errors
    stu2 = Student('sergio', 'lopez', 'string', 'string')
