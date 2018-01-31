from datetime import datetime, timedelta

from core.entities.course import Course

future_date = datetime.now() + timedelta(days=1)

def test_course_creation_from_dict():

    # Arrange
    obj = {
        'course_code': 'ASU101',
        'course_name': 'Introduction to ASU',
        'course_start': future_date
    }

    # Act
    class_1 = Course.from_dict(obj)

    # Assert
    assert class_1.course_code == "ASU101"
    assert class_1.course_name == "Introduction to ASU"
    assert class_1.course_start == future_date
