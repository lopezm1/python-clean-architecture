from datetime import datetime, timedelta

from core.entities.course import Course
from core.entities.student import Student

past_date = datetime.now() - timedelta(days=1)
future_date = datetime.now() + timedelta(days=1)


def test_student_cannot_register_after_course_start_date():

    # Arrange
    stu = Student(first_name="Miguel",
                  last_name="Lopez",
                  registered_courses=[],
                  enrolled_courses=[])
    course_1 = Course("ASU101", "Introduction to ASU", past_date)

    # Act
    result = stu.register_for_course(course=course_1)

    # Assert
    assert result is False


def test_student_can_register_before_course_start_date():

    # Arrange
    stu = Student(first_name="Miguel",
                  last_name="Lopez",
                  registered_courses=[],
                  enrolled_courses=[])
    course_1 = Course("ASU101", "Introduction to ASU", future_date)

    # Act
    result = stu.register_for_course(course=course_1)

    # Assert
    assert result is True

def test_student_cannot_register_previously_enrolled_course():

    # Arrange
    course_1 = Course("ASU101", "Introduction to ASU", past_date)
    stu = Student(first_name="Miguel",
                  last_name="Lopez",
                  registered_courses=[],
                  enrolled_courses=[course_1])
    course_2 = Course("ASU101", "Introduction to ASU", future_date)

    # Act
    result = stu.register_for_course(course=course_2)

    # Assert
    assert result is False

def test_student_creation_from_dict():

    # Arrange
    obj = {
        'first_name': 'Miguel',
        'last_name': 'Lopez',
        'registered_courses': [
            Course("ASU101", "Introduction to ASU", future_date)
        ],
        'enrolled_courses': [
            Course("CSE101", "Introduction to Engineering", past_date)
        ]
    }

    # Act
    stu = Student.from_dict(obj)

    # Assert
    assert stu.first_name == "Miguel"
    assert stu.last_name == "Lopez"
    assert len(stu.registered_courses) == 1
    assert len(stu.enrolled_courses) == 1




