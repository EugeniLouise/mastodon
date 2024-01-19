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

    def get_toot(self):
        toots = mastodon.timeline_public(limit=40)
        return toots

