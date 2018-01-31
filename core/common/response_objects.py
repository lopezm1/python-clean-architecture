class ResponseSuccess(object):
    SUCCESS = 'SUCCESS'


    def __init__(self, value=None):
        self.type = self.SUCCESS
        self.value = value

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__

"""
RESOURCE_ERROR = All errors related to resources contained in the repository. i.e. when you cannot find an entry with a unique ID
PARAMETERS_ERROR = All errors that occur when the request parameters are wrong or missing
SYSTEM_ERROR = All errors that happen in the underlying system at the operating system level. i.e. failure in filesystem operation
"""
class ResponseFailure(object):
    RESOURCE_ERROR = 'RESOURCE_ERROR'
    PARAMETERS_ERROR = 'PARAMETERS_ERROR'
    SYSTEM_ERROR = 'SYSTEM_ERROR'
    AUTH_ERROR = 'AUTHENTICATION_ERROR'

    def __init__(self, type_, message):
        self.type = type_
        self.message = self._format_message(message)

    # Enable the class to accept string messages and Python exceptions. This can be used when dealing
    # external libraries that raise exceptions.
    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return "{}: {}".format(msg.__class__.__name__, "{}".format(msg))
        return msg

    @property
    def value(self):
        return {'type': self.type, 'message': self.message}

    def __bool__(self):
        return False

    @classmethod
    def build_resource_error(cls, message=None):
        return cls(cls.RESOURCE_ERROR, message)

    @classmethod
    def build_system_error(cls, message=None):
        return cls(cls.SYSTEM_ERROR, message)

    @classmethod
    def build_parameters_error(cls, message=None):
        return cls(cls.PARAMETERS_ERROR, message)

    @classmethod
    def build_authentication_error(cls, message=None):
        return cls(cls.AUTH_ERROR, message)

    @classmethod
    def build_from_invalid_request_object(cls, invalid_request_object):
        message = "\n".join(["{}: {}".format(err['parameter'], err['message'])
                             for err in invalid_request_object.errors])

        return cls.build_parameters_error(message)