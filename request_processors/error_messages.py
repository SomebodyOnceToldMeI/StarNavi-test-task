BAD_REQUEST_ERROR_MESSAGE = {'status_code' : 400, 'message' : 'Your request has no payload or payload structure is wrong.'}

SUCCESSFULL_SIGNUP_MESSAGE = {'status_code' : 200, 'message' : 'You are successfully signed up.'}

USER_DOES_NOT_EXIST_ERROR_MESSAGE = {'status_code' : 404, 'message' : 'User does not exist.'}

SUCCESSFULL_LOGIN_MESSAGE = {'status_code' : 200, 'message' : 'You are successfully logged in.', 'access_token' : None}

INCORRECT_ACCESS_TOKEN_MESSAGE = {'status_code' : 401, 'message' : 'Provided access token is incorrect.'}

SUCCESSFULL_POST_CREATE_MESSAGE = {'status_code' : 200, 'message' : 'Post was successfully created.', 'post_id' : None}

SUCCESSFULL_LIKE_POST_MESSAGE = {'status_code' : 200, 'message' : 'Post was successfully liked.'}

SUCCESSFULL_UNLIKE_POST_MESSAGE = {'status_code' : 200, 'message' : 'Post was successfully unliked.'}
POST_WAS_NOT_LIKED_MESSAGE = {'status_code' : 400, 'message' : 'Could not unlike the post because it was not liked before.'}
