
from mastodon import Mastodon

# Initialize Mastodon API
mastodon = Mastodon(
    client_id='qkIKn3ytvhkdNQGMPuRQt14Zw0nKCmTMhWfexRHpWIc',
    client_secret='TkHuLSunv4Y6WZf6HAh_07ZHYHfIIzPdGJtzZWuJeE8',
    access_token='X0FwiBlDTKKo-FUAZ7uc26IE_cPZI1D0tFZMUzrgvP8',
    api_base_url='https://mastodon.social')

class MastodonProxy:
    def __init__(self):
        self.mastodon = mastodon

    def get_latest_toots(self, limit=50):
        toots = self.mastodon.timeline_public(limit=limit)
        return toots