from .request_processor import RequestProcessor
from .error_messages import *
import jwt

class LoginRequestProcessor(RequestProcessor):
    required_input_keys = ['login', 'password']

    def process(self):
        payload = self.request.json
        error_message = self._verify_payload(payload)
        if error_message:
            return error_message

        user = self.database.get_user(payload['login'], payload['password'])
        if not user:
            return USER_DOES_NOT_EXIST_ERROR_MESSAGE

        access_token = self._create_access_token(payload)

        message = SUCCESSFULL_LOGIN_MESSAGE.copy()
        message['access_token'] = access_token

        return message

    def _create_access_token(self, payload):
        user = self.database.get_user(payload['login'], payload['password'])

        access_token_payload = {'user_id' : user.get_id(), 'login' : user.get_login()}

        access_token = jwt.encode(access_token_payload, self.secret, algorithm='HS256')

        self.database.set_access_token_for_user(user, access_token)
        return access_token
