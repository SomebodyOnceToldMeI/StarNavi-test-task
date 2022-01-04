from .request_processor import RequestProcessor
from .error_messages import *

class CreatePostRequestProcessor(RequestProcessor):
    required_fields = ['access_token', 'post_text']

    def process(self):
        payload = self.request.json
        error_message = self._verify_payload(payload)
        if error_message:
            return error_message

        user = self.database.get_user_by_access_token(payload['access_token'])
        if not user:
            return INCORRECT_ACCESS_TOKEN_MESSAGE

        post = self.database.create_post(user, payload['post_text'])

        message = SUCCESSFULL_POST_CREATE_MESSAGE.copy()
        message['post_id'] = post.get_id()

        return message
