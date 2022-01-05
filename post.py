class Post:
    def __init__(self, text, id):
        self.text = text
        self.id = id

    def get_text(self):
        return self.text

    def get_id(self):
        return self.id
