# Test task for StarNavi

Api is built on flask.
Sqlite is used as storage.

To run:
> python server.py

## Requests:
  ### Signup request /signup
   #### Payload: 
    {"login" : login, "password" : password}
    
   Signs user up.

  ### Login request /login
   #### Payload:
      {"login" : login, "password" : password}
   #### Response:
      {"access_token" : access_token}
   Returns access_token (it expires in 1 hour).

  ### Create post request /create_post
   #### Payload:
      {"access_token" : access_token, "post_text" : post_text}
   #### Response:
      {"post_id" : post_id}
   Creates a post with requested text and returns it's id.

  ### Like post request /like_post
   #### Payload:
      {"access_token" : access_token, "post_id" : post_id}
   Adds like to a requested post.

  ### Unlike post request /unlike_post
   #### Payload:
      {"access_token" : access_token, "post_id" : post_id}
   Removes like from a requested post.

  ### Post analytics request /post_analytics
   #### Payload:
      {"access_token" : access_token, "post_id" : post_id, "date_from" date_from, "date_to" : date_to}
   #### Response:
      {"likes" : {date : number_of_likes}}
   Returns number of likes between date_from and date_to aggregated by date.
   #### date_from and date_to format:
    %d-%m-%Y ("07-01-2022")

  ### User activity request /user_activity
   #### Payload:
      {"access_token" : access_token, "user_id" : user_id}
   #### Response:
      {{"last_action" : {"action" : action, "timestamp" : timestamp}}
        "last_login" : timestamp
      }
   Returns user's last activity, last login and their timestamps.
