import sqlite3
import time
from user import User
from post import Post

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_database(self):
        create_users_table_sql = 'CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, login text, password text)'
        self.cursor.execute(create_users_table_sql)

        create_posts_table_sql = 'CREATE TABLE posts (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INT, post_text text, creation_timestamp INT)'
        self.cursor.execute(create_posts_table_sql)

        create_likes_table_sql = 'CREATE TABLE likes (user_id INT, post_id INT, creation_timestamp INT)'
        self.cursor.execute(create_likes_table_sql)

        _create_activity_table_sql = 'CREATE TABLE user_activity (user_id INT, activity TEXT, activity_timestamp INT)'
        self.cursor.execute(_create_activity_table_sql)

    def truncate_database(self):
        self.cursor.execute('DELETE FROM users;')
        self.cursor.execute('DELETE FROM posts;')
        self.cursor.execute('DELETE FROM likes;')
        self.cursor.execute('DELETE FROM user_activity;')
        self.conn.commit()


    def get_user(self, login=None, password=None, id = None):
        if id:
            self.cursor.execute('SELECT * FROM users WHERE id = ?;', (id, ))
        else:
            self.cursor.execute('SELECT * FROM users WHERE login = ? AND password = ?;', (login, password))
        user = self.cursor.fetchone()

        if user:
            user = User(login, password, user[0])
            return user
        else:
            return None


    def create_user(self, login, password):
        self.cursor.execute('INSERT INTO users (login, password) VALUES (?, ?);', (login, password))
        self.conn.commit()

        user = self.get_user(login, password)

        return user


    def create_post(self, user, post_text):
        timestamp = int(time.time())
        self.cursor.execute('INSERT INTO posts (user_id, post_text, creation_timestamp) VALUES (?, ?, ?);', (user.get_id(), post_text, timestamp))
        self.conn.commit()

        self.cursor.execute('SELECT * FROM posts WHERE user_id = ? AND post_text = ? AND creation_timestamp = ?;', (user.get_id(), post_text, timestamp))
        post = self.cursor.fetchone()
        post = Post(post[2], post[0])
        return post

    def get_post(self, post_id):
        self.cursor.execute('SELECT * FROM posts WHERE id = ?;', (post_id, ))
        post = self.cursor.fetchone()
        if post:
            post = Post(post[2], post[0])
            return post
        else:
            return None

    def get_likes_for_post(self, post):
        self.cursor.execute('SELECT * FROM likes WHERE post_id = ?;', (post.get_id(),))
        likes = self.cursor.fetchall()
        if likes:
            likes = [like[2] for like in likes] #getting like timestamp
            return likes
        else:
            return None


    def is_post_liked_by_user(self, user, post_id):
        self.cursor.execute('SELECT * FROM likes WHERE user_id = ? AND post_id = ?;', (user.get_id(), post_id))
        result = self.cursor.fetchone()
        return bool(result)

    def add_like_to_post(self, user, post_id):
        timestamp = int(time.time())
        self.cursor.execute('INSERT INTO likes (user_id, post_id, creation_timestamp) VALUES (?, ?, ?);', (user.get_id(), post_id, timestamp))
        self.conn.commit()


    def remove_like_from_post(self, user, post_id):
        self.cursor.execute('SELECT * FROM likes WHERE user_id = ? AND post_id = ?', (user.get_id(), post_id))
        like = self.cursor.fetchone()
        if not like:
            return False
        else:
            self.cursor.execute('DELETE FROM likes WHERE user_id = ? AND post_id = ?;', (user.get_id(), post_id))
            self.conn.commit()

            return True

    def create_activity(self, user, activity, timestamp = None):
        if not timestamp:
            timestamp = int(time.time())

        self.cursor.execute('INSERT INTO user_activity (user_id, activity, activity_timestamp) VALUES (?, ?, ?);', (user.get_id(), activity, timestamp))
        self.conn.commit()

    def get_last_activity_for_user(self, user):
        self.cursor.execute('SELECT * FROM user_activity WHERE user_id = ? AND activity = "login" ORDER BY activity_timestamp DESC;', (user.get_id(),))
        last_login = self.cursor.fetchone()
        if last_login:
            last_login = last_login[2]

        self.cursor.execute('SELECT * FROM user_activity WHERE user_id = ? ORDER BY activity_timestamp DESC;', (user.get_id(),))
        last_action = self.cursor.fetchone()
        if last_action:
            last_action = {'action' : last_action[1], 'timestamp' : last_action[2]}

        return last_login, last_action
