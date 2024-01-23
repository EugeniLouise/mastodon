
#definim la entities usuari i toot amb l'init dels outputs que volem

class User:
    def __init__(self, username):
        self.username = username

class Toot:
    def __init__(self, id, language, created_at, content, author):
        self.id = id
        self.language = language
        self.created_at = created_at
        self.content = content
        self.author = author


"""
user = User(username='user1234')
toot = Toot(id= "1234", language="EN", created_at="01/01/2024", content='Hola, mundo!', author=user)

print("Toot de:", toot.author.username)
print("Contenido:", toot.content)
"""

"""
class Toot:
    def __init__(self):
        self.toot_id = toot_id
        self.toot_language = toot_language
        self.toot_username = toot_username
        self.toot_created_at = toot_created_at
        self.toot_content = toot_content


toot['id']
toot['language']
toot['account']['username']
toot['content']
toot['created_at']
"""