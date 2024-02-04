from datetime import datetime


class Toot:
    def __init__(self, id: str, content: str, username: str, language: str, created_at: datetime):
        self.id = id
        self.content = content
        self.username = username
        self.language = language
        self.created_at = created_at