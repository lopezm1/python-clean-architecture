import pytest
from core.interactors.request_objects import CourseRegistrationRequestObject

@pytest.fixture
def valid_request():
    dict = {
        'personal_id': 79288,
        'course_codes': [
            "ASU101",
            "CSE110",
            "CSE120"
        ]
    }

    return dict

@pytest.fixture
def non_dict_request():
    return "Not a dictionary."

@pytest.fixture
def empty_object_error():
    return [{'parameter': 'Request Object', 'message': 'cannot be empty'}]

@pytest.fixture
def not_iterable_error():
    return [{'parameter': 'Request Object', 'message': 'not iterable.'}]

@pytest.fixture
def id_too_long_error():
    return [{'parameter': '400', 'message': 'Personal IDs must be 5 digits long.'}]

@pytest.fixture
def course_too_long_error():
    return [{'parameter': 'ClassCodeError', 'message': 'The following class code ASU1011 is too long.'}]

def test_build_course_registration_request_object_with_empty_dict(empty_object_error):
    req = CourseRegistrationRequestObject.from_dict({})

    print(req.errors)

    assert bool(req) is False
    assert req.errors == empty_object_error

def test_build_course_registration_request_object_valid_request(valid_request):
    req = CourseRegistrationRequestObject.from_dict(valid_request)

    assert bool(req) is True

def test_build_course_registration_request_object_with_string(non_dict_request, not_iterable_error):
    req = CourseRegistrationRequestObject.from_dict(non_dict_request)

    assert bool(req) is False
    assert req.errors == not_iterable_error

def test_build_course_registration_request_object_with_long_personal_id(valid_request, id_too_long_error):
    # Arrange
    valid_request['personal_id'] = 792880

    # Act
    req = CourseRegistrationRequestObject.from_dict(valid_request)

    # Assert
    assert bool(req) is False
    assert req.errors == id_too_long_error

def test_build_course_registration_request_object_with_long_course_code(valid_request, course_too_long_error):
    # Arrange
    valid_request['course_codes'][0] = "ASU1011"

    # Act
    req = CourseRegistrationRequestObject.from_dict(valid_request)

    # Assert
    assert bool(req) is False
    assert req.errors == course_too_long_error


