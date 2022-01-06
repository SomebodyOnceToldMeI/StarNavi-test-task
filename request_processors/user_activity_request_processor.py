from .request_processor import RequestProcessor
from .error_messages import *

class UserActivityRequestProcessor(RequestProcessor):
    required_input_keys = ['access_token', 'user_id']

    def process(self):
        try:
            payload = self.request.json
        except:
            payload = None
        error_message = self._verify_payload(payload)
        if error_message:
            return error_message

        user = self._verify_access_token_and_get_user(payload['access_token'])
        if not user:
            return INCORRECT_ACCESS_TOKEN_MESSAGE

        self.database.create_activity(user, 'user_activity')

        requested_user = self.database.get_user(id=payload['user_id'])
        if not requested_user:
            USER_DOES_NOT_EXIST_ERROR_MESSAGE

        last_login, last_action = self.database.get_last_activity_for_user(requested_user)
        message = {'status_code' : 200,'last_login' : last_login, 'last_action' : last_action}

        return message
