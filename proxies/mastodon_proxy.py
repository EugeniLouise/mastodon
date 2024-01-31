from mastodon import Mastodon

# Initialize Mastodon API
mastodon = Mastodon(
    client_id='qkIKn3ytvhkdNQGMPuRQt14Zw0nKCmTMhWfexRHpWIc',
    client_secret='TkHuLSunv4Y6WZf6HAh_07ZHYHfIIzPdGJtzZWuJeE8',
    access_token='X0FwiBlDTKKo-FUAZ7uc26IE_cPZI1D0tFZMUzrgvP8',
    api_base_url='https://mastodon.social')


# Mastodon API conection class
class MastodonProxy:
    def mastodon(self):
        return mastodon

    def get_toot(self, limit=100, idiomas=['en', 'es']):
        todos_toots = mastodon.timeline_public(limit=limit)
        toots_filtrados = [toot for toot in todos_toots if toot['language'] in idiomas]
        return todos_toots

