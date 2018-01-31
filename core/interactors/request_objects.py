from core.common import request_objects as req
import collections
import re



class CourseRegistrationRequestObject(req.ValidRequestObject):

    def __init__(self, personal_id: str, course_codes: list):
        self.personal_id = personal_id
        self.course_codes = course_codes

    @classmethod
    def from_dict(cls, adict):
        invalid_req = req.InvalidRequestObject()

        if not bool(adict):
            invalid_req.add_error('Request Object', 'cannot be empty')
            return invalid_req

        if not isinstance(adict, collections.Mapping):
            invalid_req.add_error('Request Object', 'not iterable.')
            return invalid_req

        if re.match('^\d{5}$', str(adict['personal_id'])) is None:
            invalid_req.add_error('400', 'Personal IDs must be 5 digits long.')

        for code in adict['course_codes']:
            if(len(code) > 6):
                invalid_req.add_error('ClassCodeError', 'The following class code ' + code + ' is too long.')

        if invalid_req.has_errors():
            return invalid_req

        return CourseRegistrationRequestObject(personal_id=adict['personal_id'],
                                               course_codes=adict['course_codes'])