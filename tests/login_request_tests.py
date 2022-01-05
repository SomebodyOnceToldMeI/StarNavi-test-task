from unittest.mock import MagicMock

import sys
import os

#add project root directory to path
if 'tests' in os.getcwd():
    parent_dir = os.path.split(os.getcwd())[0]
    sys.path.insert(0, parent_dir)
else:
    sys.path.insert(0, os.getcwd())

from request_processors.login_request_processor import LoginRequestProcessor
from request_processors.error_messages import *
from user import User

def user_gets_error_if_payload_is_incorrect():
    print('Running test: user_gets_error_if_payload_is_incorrect')

    payload = {'login' : 'test_login'} #no password
    request = MagicMock()
    request.json = payload

    database = MagicMock()

    rp = LoginRequestProcessor(request, database)
    message = rp.process()
    try:
        assert message == BAD_REQUEST_ERROR_MESSAGE
        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)


def user_gets_error_if_credentials_are_incorrect():
    print('Running test: user_gets_error_if_credentials_are_incorrect')

    payload = {'login' : 'test_login', 'password' : 'test_password'}
    request = MagicMock()
    request.json = payload

    database = MagicMock()
    database.get_user = MagicMock(return_value = False) #get_user returns True to imitate that user exists

    rp = LoginRequestProcessor(request, database)
    message = rp.process()
    try:
        assert message == USER_DOES_NOT_EXIST_ERROR_MESSAGE
        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)

def user_is_successfully_authenticated_and_receives_access_key():
    print('user_is_successfully_authenticated_and_receives_access_key')
    payload = {'login' : 'test_login', 'password' : 'test_password'}
    request = MagicMock()
    request.json = payload

    database = MagicMock()
    database.get_user = MagicMock(return_value = User('test_login', 'test_password', 1)) #get_user returns True to imitate that user exists

    rp = LoginRequestProcessor(request, database)
    message = rp.process()
    try:
        assert message.get('access_token')
        database.set_access_token_for_user.assert_called()
        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)



user_gets_error_if_payload_is_incorrect()
user_gets_error_if_credentials_are_incorrect()
user_is_successfully_authenticated_and_receives_access_key()
