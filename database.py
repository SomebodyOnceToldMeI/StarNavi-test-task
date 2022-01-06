import sqlite3
import time
from user import User

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
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


    def get_user(self, login, password, id = None):
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
        self._create_activity(user, 'registration')

        return user


    def create_post(self, user, post_text):
        timestamp = int(time.time())
        self.cursor.execute('INSERT INTO posts (user_id, post_text, creation_timestamp) VALUES (?, ?, ?);', (user.get_id(), post_text, timestamp))
        self.conn.commit()

        self._create_activity(user, 'create_post', timestamp=timestamp)


    def add_like_to_post(self, user, post_id):
        timestamp = int(time.time())
        self.cursor.execute('INSERT INTO likes (user_id, post_id, creation_timestamp) VALUES (?, ?, ?);', (user.get_id(), post_id, timestamp))
        self.conn.commit()

        self._create_activity(user, 'like_post', timestamp=timestamp)

    def remove_like_from_post(self, user, post_id):
        self.cursor.execute('DELETE FROM likes WHERE user_id = ? AND post_id = ?;', (user.get_id(), post_id))
        self.conn.commit()

        self._create_activity(user, 'unlike_post')

    def _create_activity(self, user, activity, timestamp = None):
        if not timestamp:
            timestamp = int(time.time())

        self.cursor.execute('INSERT INTO user_activity (user_id, activity, activity_timestamp) VALUES (?, ?, ?);', (user.get_id(), activity, timestamp))
        self.conn.commit()
