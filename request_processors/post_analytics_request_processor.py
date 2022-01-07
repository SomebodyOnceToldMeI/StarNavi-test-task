from .request_processor import RequestProcessor
from .response_messages import *

import datetime

class PostAnalyticsRequestProcessor(RequestProcessor):
    required_input_keys = ['access_token', 'post_id', 'date_from', 'date_to']

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

        self.database.create_activity(user, 'post_analytics')

        post = self.database.get_post(payload['post_id'])
        if not post:
            return POST_DOES_NOT_EXIST_MESSAGE

        likes = self.database.get_likes_for_post(post)

        date_from = datetime.datetime.strptime(payload['date_from'], '%d-%m-%Y').date()
        date_to = datetime.datetime.strptime(payload['date_to'], '%d-%m-%Y').date()
        aggregated_likes = self._aggregate_likes_by_day_from_date_to_date(likes,date_from ,date_to )

        message = {'status_code' : 200, 'likes' : aggregated_likes}

        return message

    def _aggregate_likes_by_day_from_date_to_date(self, likes, date_from, date_to):
        aggregated_likes = {}
        for like in likes:
            date = datetime.datetime.fromtimestamp(like).date()
            if not date >= date_from or not date <= date_to:
                continue

            str_date = date.strftime('%d-%m-%Y')

            aggregated_likes[str_date] = aggregated_likes.get(str_date, 0) + 1

        return aggregated_likes
