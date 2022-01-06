from .request_processor import RequestProcessor
from .error_messages import *
import jwt
import datetime

class LoginRequestProcessor(RequestProcessor):
    required_input_keys = ['login', 'password']

    def process(self):
        try:
            payload = self.request.json
        except:
            payload = None
        error_message = self._verify_payload(payload)
        if error_message:
            return error_message

        user = self.database.get_user(payload['login'], payload['password'])
        if not user:
            return USER_DOES_NOT_EXIST_ERROR_MESSAGE


        self.database.create_activity(user, 'login')
        expiration_timestamp = int((datetime.datetime.now() + datetime.timedelta(hours=1)).timestamp())
        access_token = self._create_access_token(payload, expiration_timestamp)

        message = SUCCESSFULL_LOGIN_MESSAGE.copy()
        message['access_token'] = access_token

        return message

    def _create_access_token(self, payload, expiration_timestamp):
        user = self.database.get_user(payload['login'], payload['password'])

        access_token_payload = {'user_id' : user.get_id(), 'login' : user.get_login(), 'expiration_timestamp' : expiration_timestamp}

        access_token = jwt.encode(access_token_payload, self.secret, algorithm='HS256')

        return access_token
