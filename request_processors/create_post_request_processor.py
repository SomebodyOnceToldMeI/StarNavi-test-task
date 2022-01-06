from .request_processor import RequestProcessor
from .error_messages import *

class CreatePostRequestProcessor(RequestProcessor):
    required_input_keys = ['access_token', 'post_text']

    def process(self):
        payload = self.request.json
        error_message = self._verify_payload(payload)
        if error_message:
            return error_message

        user = self._verify_access_token_and_get_user(payload['access_token'])
        if not user:
            return INCORRECT_ACCESS_TOKEN_MESSAGE

        post = self.database.create_post(user, payload['post_text'])

        message = SUCCESSFULL_POST_CREATE_MESSAGE.copy()
        message['post_id'] = post.get_id()

        return message
