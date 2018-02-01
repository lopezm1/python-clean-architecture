from core.interfaces.person_interface import PersonInterface

from core.common import response_objects as res
from core.common.interactor import Interactor
from core.interfaces.course_interface import CourseInterface


class CourseRegistrationInteractor(Interactor):

    def __init__(self, auth_service,
                 person_repo: PersonInterface,
                 course_repo: CourseInterface):
        self._auth_service = auth_service
        self._person_repo = person_repo
        self._course_repo = course_repo

    def process_request(self, request_object):

        # Check authentication service
        if(not self._auth_service.is_logged_in()):
            return res.ResponseFailure.build_authentication_error("Access denied, User not authenticated.")

        # Get person object
        person = self._person_repo.get_by_id(personal_id=request_object.personal_id)

        errors = []

        for code in request_object.course_codes:
            # Get course object
            course = self._course_repo.get_by_code(code=code)

            # Attempt to register for course
            if(not person.register_for_course(course)):
                errors.append("Unable to register for " + code)

        # Save student
        self._person_repo.save(person=person)

        # Allow the user to see any failed class registrations
        return res.ResponseSuccess(errors)








