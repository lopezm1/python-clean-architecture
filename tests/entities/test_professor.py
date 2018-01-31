from datetime import datetime, timedelta

from core.entities.course import Course
from core.entities.professor import Professor

past_date = datetime.now() - timedelta(days=1)
future_date = datetime.now() + timedelta(days=1)


def test_professor_cannot_teach_same_course_more_than_3times():

    # Arrange
    course_1 = Course("ASU101", "Introduction to ASU", past_date)
    course_2 = Course("ASU101", "Introduction to ASU", past_date)
    course_3 = Course("ASU101", "Introduction to ASU", past_date)
    course_4 = Course("ASU101", "Introduction to ASU", future_date)
    prof = Professor(first_name="Miguel",
                  last_name="Lopez",
                  semester_courses=[],
                  course_history=[course_1, course_2, course_3])

    # Act
    result = prof.register_for_course(course_4)

    # Assert
    assert result is False

def test_professor_cannot_teach_more_than_5_courses_in_semester():

    # Arrange
    course_1 = Course("ASU101", "Introduction to ASU", future_date)
    course_2 = Course("ASU101", "Introduction to ASU", future_date)
    course_3 = Course("CSE101", "Introduction to Engineering", future_date)
    course_4 = Course("CSE101", "Introduction to Engineering", future_date)
    course_5 = Course("ART101", "Introduction to Art", future_date)
    course_6 = Course("ART101", "Introduction to Art", future_date)
    prof = Professor(first_name="Miguel",
                  last_name="Lopez",
                  semester_courses=[course_1, course_2, course_3, course_4, course_5],
                  course_history=[])

    # Act
    result = prof.register_for_course(course_6)

    # Assert
    assert result is False

def test_professor_cannot_teach_class_that_started_in_past():

    # Arrange
    course_1 = Course("ASU101", "Introduction to ASU", past_date)
    prof = Professor(first_name="Miguel",
                     last_name="Lopez",
                     semester_courses=[],
                     course_history=[])

    # Act
    result = prof.register_for_course(course_1)

    # Assert
    assert result is False

def test_professor_successfully_registers_to_teach_class():

    # Arrange
    course_1 = Course("ASU101", "Introduction to ASU", future_date)
    prof = Professor(first_name="Miguel",
                     last_name="Lopez",
                     semester_courses=[],
                     course_history=[])

    # Act
    result = prof.register_for_course(course_1)

    # Assert
    assert result is True

def test_profession_creation_from_dict():

    # Arrange
    obj = {
        'first_name': 'Miguel',
        'last_name': 'Lopez',
        'semester_courses': [
            Course("ASU101", "Introduction to ASU", future_date)
        ],
        'course_history': [
            Course("CSE101", "Introduction to Engineering", past_date)
        ]
    }

    # Act
    prof = Professor.from_dict(obj)

    # Assert
    assert prof.first_name == "Miguel"
    assert prof.last_name == "Lopez"
    assert len(prof.semester_courses) == 1
    assert len(prof.course_history) == 1