
#general
BAD_REQUEST_ERROR_MESSAGE = {'status_code' : 400, 'message' : 'Your request has no payload or payload structure is wrong.'}
INCORRECT_ACCESS_TOKEN_MESSAGE = {'status_code' : 401, 'message' : 'Provided access token is incorrect or it is expired.'}
USER_DOES_NOT_EXIST_ERROR_MESSAGE = {'status_code' : 404, 'message' : 'User does not exist.'}
POST_DOES_NOT_EXIST_MESSAGE = {'status_code' : 400, 'message' : 'Post you tried to interact does not exist.'}

#signup
USER_IS_ALREADY_SIGNED_UP = {'status_code' : 400, 'message' : 'User with inserted credentials is already signed up.'}
SUCCESSFULL_SIGNUP_MESSAGE = {'status_code' : 200, 'message' : 'You are successfully signed up.'}

#login
SUCCESSFULL_LOGIN_MESSAGE = {'status_code' : 200, 'message' : 'You are successfully logged in.', 'access_token' : None}

#create post
SUCCESSFULL_POST_CREATE_MESSAGE = {'status_code' : 200, 'message' : 'Post was successfully created.', 'post_id' : None}

#like post
SUCCESSFULL_LIKE_POST_MESSAGE = {'status_code' : 200, 'message' : 'Post was successfully liked.'}
POST_IS_ALREADY_LIKED_MESSAGE = {'status_code' : 400, 'message' : 'Post was not liked because it was already liked before.'}

#unlike post
SUCCESSFULL_UNLIKE_POST_MESSAGE = {'status_code' : 200, 'message' : 'Post was successfully unliked.'}
POST_WAS_NOT_LIKED_MESSAGE = {'status_code' : 400, 'message' : 'Could not unlike the post because it was not liked before.'}
