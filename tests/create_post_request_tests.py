from unittest.mock import MagicMock

import sys
import os

#add project root directory to path
if 'tests' in os.getcwd():
    parent_dir = os.path.split(os.getcwd())[0]
    sys.path.insert(0, parent_dir)
else:
    sys.path.insert(0, os.getcwd())

from request_processors.create_post_request_processor import CreatePostRequestProcessor
from request_processors.error_messages import *
from user import User
from post import Post

def user_gets_error_if_payload_is_incorrect():
    print('Running test: user_gets_error_if_payload_is_incorrect')

    payload = {'login' : 'test_login'} #no password
    request = MagicMock()
    request.json = payload

    database = MagicMock()

    rp = CreatePostRequestProcessor(request, database)
    message = rp.process()
    try:
        assert message == BAD_REQUEST_ERROR_MESSAGE
        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)


def user_gets_error_if_access_token_is_incorrect():
    print('Running test: user_gets_error_if_access_token_is_incorrect')

    payload = {'access_token' : 'token', 'post_text' : 'text'}
    request = MagicMock()
    request.json = payload

    database = MagicMock()
    database.get_user_by_access_token = MagicMock(return_value = False) #get_user returns True to imitate that user exists

    rp = CreatePostRequestProcessor(request, database)
    message = rp.process()
    try:
        assert message == INCORRECT_ACCESS_TOKEN_MESSAGE
        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)

def post_is_successfully_created_and_user_gets_success_message_if_token_is_correct():
    print('post_is_successfully_created_and_user_gets_success_message_if_token_is_correct')
    payload = {'access_token' : 'token', 'post_text' : 'text'}
    request = MagicMock()
    request.json = payload

    database = MagicMock()
    database.get_user_by_access_token = MagicMock(return_value = User('test_login', 'test_password', 1)) #get_user returns True to imitate that user exists
    database.create_post = MagicMock(return_value = Post('text', 1))

    rp = CreatePostRequestProcessor(request, database)
    message = rp.process()
    try:
        assert message.get('post_id')

        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)



user_gets_error_if_payload_is_incorrect()
user_gets_error_if_access_token_is_incorrect()
post_is_successfully_created_and_user_gets_success_message_if_token_is_correct()
