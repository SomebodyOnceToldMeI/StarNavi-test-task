from .error_messages import BAD_REQUEST_ERROR_MESSAGE
import jwt

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
        token_payload = jwt.decode(access_token, self.secret, algorithms = ['HS256'])
        user = self.database.get_user(id = token_payload['user_id'])
        return user
