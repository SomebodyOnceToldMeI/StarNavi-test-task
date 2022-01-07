from unittest.mock import MagicMock

import sys
import os

#add project root directory to path
if 'tests' in os.getcwd():
    parent_dir = os.path.split(os.getcwd())[0]
    sys.path.insert(0, parent_dir)
else:
    sys.path.insert(0, os.getcwd())

from request_processors.user_activity_request_processor import UserActivityRequestProcessor
from request_processors.response_messages import *
from user import User
from post import Post

def user_gets_error_if_payload_is_incorrect():
    print('Running test: user_gets_error_if_payload_is_incorrect')

    payload = {'login' : 'test_login'} #no password
    request = MagicMock()
    request.json = payload

    database = MagicMock()

    rp = UserActivityRequestProcessor(request, database)
    message = rp.process()
    try:
        assert message == BAD_REQUEST_ERROR_MESSAGE
        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)


def user_gets_error_if_access_token_is_incorrect():
    print('Running test: user_gets_error_if_access_token_is_incorrect')

    payload = {'access_token' : 'token', 'user_id' : 1}
    request = MagicMock()
    request.json = payload

    database = MagicMock()
    database.get_user_by_access_token = MagicMock(return_value = False) #returns false like user does not exist

    rp = UserActivityRequestProcessor(request, database)
    message = rp.process()
    try:
        assert message == INCORRECT_ACCESS_TOKEN_MESSAGE
        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)

def user_gets_error_if_requested_user_does_not_exist():
    print('Running test: user_gets_error_if_requested_user_does_not_exist')
    payload = {'access_token' : 'token', 'user_id' : 1}
    request = MagicMock()
    request.json = payload

    database = MagicMock()
    database.get_user = MagicMock(return_value = None)

    user = User('test_login', 'test_password', 1)
    rp = UserActivityRequestProcessor(request, database)
    rp._verify_access_token_and_get_user = MagicMock(return_value = user)
    message = rp.process()
    try:
        assert message == USER_DOES_NOT_EXIST_ERROR_MESSAGE

        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)

def user_successfully_gets_activity():
    print('Running test: user_successfully_gets_activity')
    payload = {'access_token' : 'token', 'user_id' : 2}
    request = MagicMock()
    request.json = payload

    database = MagicMock()
    requested_user = User('test_login', 'test_password', 2)
    database.get_user = MagicMock(return_value = requested_user)
    database.get_last_activity_for_user = MagicMock(return_value = (True, True))

    user = User('test_login', 'test_password', 1)
    rp = UserActivityRequestProcessor(request, database)
    rp._verify_access_token_and_get_user = MagicMock(return_value = user)
    message = rp.process()
    try:
        assert message['status_code'] == 200
        assert message['last_login'] == True
        assert message['last_action'] == True

        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)



user_gets_error_if_payload_is_incorrect()
user_gets_error_if_access_token_is_incorrect()
user_gets_error_if_requested_user_does_not_exist()
user_successfully_gets_activity()
