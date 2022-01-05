from unittest.mock import MagicMock

import sys
import os

#add project root directory to path
if 'tests' in os.getcwd():
    parent_dir = os.path.split(os.getcwd())[0]
    sys.path.insert(0, parent_dir)
else:
    sys.path.insert(0, os.getcwd())

from request_processors.signup_request_processor import SignupRequestProcessor
from request_processors.error_messages import *

def user_gets_error_if_payload_is_incorrect():
    print('Running test: user_gets_error_if_payload_is_incorrect')

    payload = {'login' : 'test_login'} #no password
    request = MagicMock()
    request.json = payload

    database = MagicMock()

    rp = SignupRequestProcessor(request, database)
    message = rp.process()
    try:
        assert message == BAD_REQUEST_ERROR_MESSAGE
        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)


def user_gets_error_if_is_already_registered_and_user_is_not_created_in_database():
    print('Running test: user_gets_error_if_is_already_registered_and_user_is_not_created_in_database')

    payload = {'login' : 'test_login', 'password' : 'test_password'}
    request = MagicMock()
    request.json = payload

    database = MagicMock()
    database.get_user = MagicMock(return_value = True) #get_user returns True to imitate that user exists

    rp = SignupRequestProcessor(request, database)
    message = rp.process()
    try:
        assert message == USER_IS_ALREADY_SIGNED_UP
        database.create_user.assert_not_called()
        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)

def user_is_successfully_registered():
    print('Running test: user_is_successfully_registered')
    payload = {'login' : 'test_login', 'password' : 'test_password'}
    request = MagicMock()
    request.json = payload

    database = MagicMock()
    database.get_user = MagicMock(return_value = False) #get_user returns True to imitate that user exists

    rp = SignupRequestProcessor(request, database)
    message = rp.process()
    try:
        assert message == SUCCESSFULL_SIGNUP_MESSAGE
        database.create_user.assert_called()
        print('Test passed.')
    except:
        print('Test failed.')
        print('Returned message: ', message)


user_gets_error_if_payload_is_incorrect()
user_gets_error_if_is_already_registered_and_user_is_not_created_in_database()
user_is_successfully_registered()
