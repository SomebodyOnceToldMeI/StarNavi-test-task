from unittest.mock import MagicMock

import sys
import os

#add project root directory to path
if 'tests' in os.getcwd():
    parent_dir = os.path.split(os.getcwd())[0]
    sys.path.insert(0, parent_dir)
else:
    sys.path.insert(0, os.getcwd())

from request_processors.post_analytics_request_processor import PostAnalyticsRequestProcessor
from request_processors.response_messages import *
from user import User
from post import Post

def user_gets_error_if_payload_is_incorrect():
    print('Running test: user_gets_error_if_payload_is_incorrect')

    payload = {'login' : 'test_login'} #no password
    request = MagicMock()
    request.json = payload

    database = MagicMock()

    rp = PostAnalyticsRequestProcessor(request, database)
    message = rp.process()
    try:
        assert message == BAD_REQUEST_ERROR_MESSAGE
        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)


def user_gets_error_if_access_token_is_incorrect():
    print('Running test: user_gets_error_if_access_token_is_incorrect')

    payload = {'access_token' : 'token', 'post_id' : 1, 'date_from' : 1, 'date_to' : 2}
    request = MagicMock()
    request.json = payload

    database = MagicMock()
    database.get_user_by_access_token = MagicMock(return_value = False)#returns false like user does not exist

    rp = PostAnalyticsRequestProcessor(request, database)
    message = rp.process()
    try:
        assert message == INCORRECT_ACCESS_TOKEN_MESSAGE
        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)

def user_gets_error_if_requested_post_does_not_exist():
    print('Running test: user_gets_error_if_requested_post_does_not_exist')
    payload = {'access_token' : 'token', 'post_id' : 1, 'date_from' : 1, 'date_to' : 2}
    request = MagicMock()
    request.json = payload

    database = MagicMock()
    database.get_post = MagicMock(return_value = None)

    user = User('test_login', 'test_password', 1)
    rp = PostAnalyticsRequestProcessor(request, database)
    rp._verify_access_token_and_get_user = MagicMock(return_value = user)
    message = rp.process()
    try:
        assert message == POST_DOES_NOT_EXIST_MESSAGE

        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)

def user_successfully_gets_aggregated_likes():
    print('Running test: user_successfully_gets_aggregated_likes')
    payload = {'access_token' : 'token', 'post_id' : 1, 'date_from' : '05-01-2022', 'date_to' : '06-01-2022'}
    request = MagicMock()
    request.json = payload

    database = MagicMock()

    database.get_post = MagicMock(return_value = True)
    likes = [1641380507, 1641380508, 1641380509, 1641380510, 1641466907, 1641466908, 1641553307, 1641553308, 1641553309]
    database.get_likes_for_post = MagicMock(return_value = likes)


    user = User('test_login', 'test_password', 1)
    rp = PostAnalyticsRequestProcessor(request, database)
    rp._verify_access_token_and_get_user = MagicMock(return_value = user)
    message = rp.process()
    try:
        assert message['likes'] == {'05-01-2022': 4, '06-01-2022': 2}

        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)



user_gets_error_if_payload_is_incorrect()
user_gets_error_if_access_token_is_incorrect()
user_gets_error_if_requested_post_does_not_exist()
user_successfully_gets_aggregated_likes()
