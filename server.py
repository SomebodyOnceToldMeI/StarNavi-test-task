from flask import Flask, request
from error_messages import *

app = Flask(__name__)

@app.route('/signup')
def signup():
    request_payload = request.json
    if not request_payload:
        return EMPTY_REQUEST_ERROR_MESSAGE

@app.route('/login')
def login():
    request_payload = request.json
    if not request_payload:
        return EMPTY_REQUEST_ERROR_MESSAGE

@app.route('/create_post')
def create_post():
    request_payload = request.json
    if not request_payload:
        return EMPTY_REQUEST_ERROR_MESSAGE

@app.route('/like_post')
def like_post():
    request_payload = request.json
    if not request_payload:
        return EMPTY_REQUEST_ERROR_MESSAGE

@app.route('/unlike_post')
def unlike_post():
    request_payload = request.json
    if not request_payload:
        return EMPTY_REQUEST_ERROR_MESSAGE

@app.route('/post_analytics')
def post_analytics():
    request_payload = request.json
    if not request_payload:
        return EMPTY_REQUEST_ERROR_MESSAGE

@app.route('/user_activity')
def user_activity():
    request_payload = request.json
    if not request_payload:
        return EMPTY_REQUEST_ERROR_MESSAGE

if __name__ == '__main__':
    app.run(host='localhost', port='8080')
