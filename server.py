from flask import Flask, request
from request_processors.signup_request_processor import SignupRequestProcessor
from request_processors.login_request_processor import LoginRequestProcessor
from request_processors.create_post_request_processor import CreatePostRequestProcessor
from request_processors.like_post_request_processor import LikePostRequestProcessor
from request_processors.unlike_post_request_processor import UnlikePostRequestProcessor
from request_processors.user_activity_request_processor import UserActivityRequestProcessor
from request_processors.post_analytics_request_processor import PostAnalyticsRequestProcessor

from database import Database
import os
if not os.path.exists('database.db'):
    db = Database()
    db.create_database()
else:
    db = Database()

app = Flask(__name__)

@app.route('/signup')
def signup():
    rp = SignupRequestProcessor(request, db)
    response = rp.process()
    return response

@app.route('/login')
def login():
    rp = LoginRequestProcessor(request, db)
    response = rp.process()
    return response

@app.route('/create_post')
def create_post():
    rp = CreatePostRequestProcessor(request, db)
    response = rp.process()
    return response

@app.route('/like_post')
def like_post():
    rp = LikePostRequestProcessor(request, db)
    response = rp.process()
    return response

@app.route('/unlike_post')
def unlike_post():
    rp = UnlikePostRequestProcessor(request, db)
    response = rp.process()
    return response

@app.route('/post_analytics')
def post_analytics():
    rp = PostAnalyticsRequestProcessor(request, db)
    response = rp.process()
    return response

@app.route('/user_activity')
def user_activity():
    rp = UserActivityRequestProcessor(request, db)
    response = rp.process()
    return response

if __name__ == '__main__':
    app.run(host='localhost', port='8080')
