from .request_processor import RequestProcessor
from .error_messages import *

class UnlikePostRequestProcessor(RequestProcessor):
    required_input_keys = ['access_token', 'post_id']

    def process(self):
        payload = self.request.json
        error_message = self._verify_payload(payload)
        if error_message:
            return error_message

        user = self.database.get_user_by_access_token(payload['access_token'])
        if not user:
            return INCORRECT_ACCESS_TOKEN_MESSAGE

        if self.database.remove_like_from_post(user, payload['post_id']):
            return SUCCESSFULL_UNLIKE_POST_MESSAGE
        else:
            return POST_WAS_NOT_LIKED_MESSAGE
