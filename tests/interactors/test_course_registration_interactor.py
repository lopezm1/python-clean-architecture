import pytest
from unittest import mock
from core.interactors.request_objects import CourseRegistrationRequestObject
from core.interactors.course_registration_interactor import CourseRegistrationInteractor
from core.entities.student import Student
from core.entities.course import Course
from datetime import datetime, timedelta

future_date = datetime.now() + timedelta(days=1)
past_date = datetime.now() - timedelta(days=1)


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
def return_5_classes():
    courses = [
        Course("ASU101", "Introduction to ASU", future_date),
        Course("CSE110", "Introduction to Java", future_date),
        Course("CSE120", "Introduction to Logic", future_date),
        Course("PHY101", "Physics 101", future_date),
        Course("MAT225", "Calculus 2", future_date)
    ]
    return courses

@pytest.fixture
def return_past_date_classes():
    courses = [
        Course("ASU101", "Introduction to ASU", past_date),
        Course("CSE110", "Introduction to Java", past_date),
        Course("CSE120", "Introduction to Logic", past_date)
    ]
    return courses


def test_user_not_logged_in(valid_request):

    # Arrange
    _auth_service = mock.Mock()
    _person_repo = mock.Mock()
    _course_repo = mock.Mock()
    _auth_service.is_logged_in.return_value = False

    req_object = CourseRegistrationRequestObject.from_dict(valid_request)
    interactor = CourseRegistrationInteractor(auth_service=_auth_service,
                                              person_repo=_person_repo,
                                              course_repo=_course_repo)

    # Act
    response = interactor.execute(req_object)

    # Assert
    assert bool(response) is False
    assert response.type == "AUTHENTICATION_ERROR"
    _auth_service.is_logged_in.assert_called()
    _person_repo.get_by_id.assert_not_called()
    _course_repo.get_by_code.assert_not_called()
    _person_repo.save.assert_not_called()


def test_user_register_first_3_classes_ever(valid_request, return_5_classes):

    # Arrange
    _auth_service = mock.Mock()
    _person_repo = mock.Mock()
    _course_repo = mock.Mock()
    _auth_service.is_logged_in.return_value = True
    _person_repo.get_by_id.return_value = Student("Miguel", "Lopez", [], [])
    _course_repo.get_by_code.side_effect = return_5_classes

    req_object = CourseRegistrationRequestObject.from_dict(valid_request)
    interactor = CourseRegistrationInteractor(auth_service=_auth_service,
                                              person_repo=_person_repo,
                                              course_repo=_course_repo)

    # Act
    response = interactor.execute(req_object)

    # Assert
    assert bool(response) is True
    _auth_service.is_logged_in.assert_called()
    _person_repo.get_by_id.assert_called()
    _course_repo.get_by_code.assert_called()
    _person_repo.save.assert_called()

def test_user_register_3_errors_with_already_enrolled_classes(valid_request, return_5_classes):

    # Arrange
    _auth_service = mock.Mock()
    _person_repo = mock.Mock()
    _course_repo = mock.Mock()
    _auth_service.is_logged_in.return_value = True
    _person_repo.get_by_id.return_value = Student("Miguel", "Lopez", [], return_5_classes)
    _course_repo.get_by_code.side_effect = return_5_classes

    req_object = CourseRegistrationRequestObject.from_dict(valid_request)
    interactor = CourseRegistrationInteractor(auth_service=_auth_service,
                                              person_repo=_person_repo,
                                              course_repo=_course_repo)

    # Act
    response = interactor.execute(req_object)

    # Assert
    assert bool(response) is True
    assert len(response.value) == 3
    _auth_service.is_logged_in.assert_called()
    _person_repo.get_by_id.assert_called()
    _course_repo.get_by_code.assert_called()
    _person_repo.save.assert_called()

def test_user_register_3_errors_with_past_start_time_course(valid_request, return_past_date_classes):

    # Arrange
    _auth_service = mock.Mock()
    _person_repo = mock.Mock()
    _course_repo = mock.Mock()
    _auth_service.is_logged_in.return_value = True
    _person_repo.get_by_id.return_value = Student("Miguel", "Lopez", [], [])
    _course_repo.get_by_code.side_effect = return_past_date_classes

    req_object = CourseRegistrationRequestObject.from_dict(valid_request)
    interactor = CourseRegistrationInteractor(auth_service=_auth_service,
                                              person_repo=_person_repo,
                                              course_repo=_course_repo)

    # Act
    response = interactor.execute(req_object)

    # Assert
    assert bool(response) is True
    assert len(response.value) == 3
    _auth_service.is_logged_in.assert_called()
    _person_repo.get_by_id.assert_called()
    _course_repo.get_by_code.assert_called()
    _person_repo.save.assert_called()