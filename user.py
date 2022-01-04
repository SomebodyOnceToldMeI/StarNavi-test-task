class User:
    def __init__(self, login, password, id):
        self.login = login
        self.password = password
        self.id = id

    def get_login(self):
        return self.login

    def get_password(self):
        return self.password

    def get_id(self):
        return self.id
