from .request_processor import RequestProcessor
from .response_messages import *

class UnlikePostRequestProcessor(RequestProcessor):
    required_input_keys = ['access_token', 'post_id']

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

        self.database.create_activity(user, 'unlike_post')
        post = self.database.get_post(payload['post_id'])

        if post:

            if self.database.remove_like_from_post(user, post.get_id()):
                return SUCCESSFULL_UNLIKE_POST_MESSAGE
            else:
                return POST_WAS_NOT_LIKED_MESSAGE
        else:
            return POST_DOES_NOT_EXIST_MESSAGE
