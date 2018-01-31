from datetime import datetime
from typing import List

from core.common.entity_model import EntityModel
from core.entities.course import Course

# Custom TypeCheck for List of Courses
CourseList = List[Course]

class Professor(EntityModel):

    def __init__(self, first_name: str, last_name: str,
                 semester_courses: CourseList,
                 course_history: CourseList):
        self.first_name = first_name
        self.last_name = last_name
        self.semester_courses = semester_courses[:]
        self.course_history = course_history[:]
    # Opted to create new list objects[:] to enforce object creation
    # Developers won't see lists shared amongst Professor objects unintentionally

    @classmethod
    def from_dict(cls, adict):
        return cls(adict['first_name'],
                   adict['last_name'],
                   adict['semester_courses'][:],
                   adict['course_history'][:])
    ## using [:] to make a copy and pass a reference to a new object
    ## prevents weirdness that happens with mutable lists by having unique memory location

    def register_for_course(self, course: Course):

        # Professor cannot teach a class that started in the past
        if (datetime.now() > course.course_start):
            return False

        # Professor cannot teach more than 5 courses in a semester
        if(len(self.semester_courses) > 4):
            return False

        # Professor cannot teach the same course 3 times
        if(sum(x.course_code == course.course_code for x in self.course_history) >= 3):
            return False

        self.semester_courses.append(course)
        return True



if __name__ == "__main__":

    old_date = datetime.strptime('2012-08-21', '%Y-%m-%d')
    new_date = datetime.strptime('2022-08-21', '%Y-%m-%d')
    obj = {
        'first_name': 'miguel',
        'last_name': 'lopez',
        'semester_courses': [
            Course('ASU101','Introduction to ASU', old_date),
            Course('ASU101', 'Introduction to ASU', old_date),
            Course('CSE100','Introduction to Java', old_date),
            Course('CSE100', 'Introduction to Java', old_date),
        ],
        'course_history': [
            Course('CSE110','Circuits', old_date),
            Course('CSE110', 'Circuits', old_date),
            Course('CSE110', 'Circuits', old_date),
            Course('CSE255','Data Structures and Algorithms', old_date),
            Course('ART410','Advanced Art', old_date),
        ]
    }

    too_many_enroll = Course('CSE110', 'Circuits', new_date)
    first_enroll = Course('CSE120', 'Logic Boards', old_date)
    double_enroll = Course('CSE360', 'Intro to Software Engineering', new_date)

    prof1 = Professor.from_dict(obj)
    prof2 = Professor.from_dict(obj)
    print(id(prof1.course_history))
    print(id(prof2.course_history))

    print("Length of (prof1.semester_courses, prof1.course_history):", len(prof1.semester_courses),
          len(prof1.course_history))
    # Prints false bc professor can't teach same class more than 3 times
    print("Professor 1 - Same class more than 3 times class history:", prof1.register_for_course(too_many_enroll))
    print("Length of (prof1.semester_courses, prof1.course_history):", len(prof1.semester_courses),
          len(prof1.course_history))
    # Prints true because professor has 5 classes
    print("Professor 1 - New class, less than 5 classes:", prof1.register_for_course(first_enroll))
    print("Length of (prof1.semester_courses, prof1.course_history):", len(prof1.semester_courses),
          len(prof1.course_history))

    print("\n")
    print("Length of (prof2.semester_courses, prof2.course_history):", len(prof2.semester_courses),
          len(prof2.course_history))
    # Prints true because professor has 5 classes
    print("Professor 2 - New class, less than 5 classes:", prof2.register_for_course(first_enroll))
    print("Length of (prof2.semester_courses, prof2.course_history):", len(prof2.semester_courses),
          len(prof2.course_history))
    # Prints false bc professor can't teach more than 5 classes
    print("Professor 2 - New class, more than 5 classes:", prof2.register_for_course(double_enroll))
    print("Length of (prof2.semester_courses, prof2.course_history):", len(prof2.semester_courses),
          len(prof2.course_history))

    print("\nTESTING MEMORY REFERENCES FROM __INIT__")
    prof3 = Professor("Prof3", "Test", obj['semester_courses'], obj['course_history'])
    prof4 = Professor("Prof4", "Test", obj['semester_courses'], obj['course_history'])
    print("Memory ID of prof3.semester_course:", id(prof3.semester_courses))
    print("Memory ID of prof4.semester_course:", id(prof4.semester_courses))

