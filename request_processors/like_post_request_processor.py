from .request_processor import RequestProcessor
from .error_messages import *

class LikePostRequestProcessor(RequestProcessor):
    required_input_keys = ['access_token', 'post_id']

    def process(self):
        payload = self.request.json
        error_message = self._verify_payload(payload)
        if error_message:
            return error_message

        user = self._verify_access_token_and_get_user(payload['access_token'])
        if not user:
            return INCORRECT_ACCESS_TOKEN_MESSAGE

        self.database.add_like_to_post(user, payload['post_id'])
        return SUCCESSFULL_LIKE_POST_MESSAGE
