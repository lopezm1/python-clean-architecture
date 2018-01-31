import pytest
from unittest import mock
from core.interactors.request_objects import CourseRegistrationRequestObject
from core.interactors.course_registration_interactor import CourseRegistrationInteractor
from core.entities.student import Student

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
    _auth_service.is_logged_in.assert_called()
    _person_repo.get_by_id.assert_not_called()
    _course_repo.get_by_code.assert_not_called()
    _person_repo.save.assert_not_called()

