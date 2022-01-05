from .request_processor import RequestProcessor
from .error_messages import *

class SignupRequestProcessor(RequestProcessor):
    required_input_keys = ['login', 'password']

    def process(self):
        payload = self.request.json
        error_message = self._verify_payload(payload)
        if error_message:
            return error_message

        user = self.database.get_user(payload['login'], payload['password'])
        if not user:
            self.database.create_user(payload['login'],payload['password'])
        else:
            return USER_IS_ALREADY_SIGNED_UP

        return SUCCESSFULL_SIGNUP_MESSAGE
