from .response_messages import BAD_REQUEST_ERROR_MESSAGE
import jwt
import datetime

class RequestProcessor:
    secret = 'secret'
    required_input_keys = [] #keys that request payload has to contain

    def __init__(self, request, database):
        self.request = request
        self.database = database

    def process(self):
        pass

    def _verify_payload(self, payload):
        if not payload:
            return BAD_REQUEST_ERROR_MESSAGE

        for key in self.required_input_keys:
            if not key in payload.keys():
                return BAD_REQUEST_ERROR_MESSAGE

        for key in self.required_input_keys:
            if not payload[key]:
                return BAD_REQUEST_ERROR_MESSAGE

    def _verify_access_token_and_get_user(self, access_token):
        try:
            token_payload = jwt.decode(access_token, self.secret, algorithms = ['HS256'])
        except:
            return None
        if token_payload['expiration_timestamp'] < datetime.datetime.now().timestamp():
            return None

        user = self.database.get_user(id = token_payload['user_id'])
        return user
