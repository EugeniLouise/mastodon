
from mastodon import Mastodon
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='C:/Users/Eugenia Subirons/PycharmProjects/Mastodon_G/proxy/credentials.env')

# Initialize Mastodon API
mastodon = Mastodon(
    client_id=os.getenv('MASTODON_CLIENT_ID'),
    client_secret=os.getenv('MASTODON_CLIENT_SECRET'),
    access_token=os.getenv('MASTODON_ACCESS_TOKEN'),
    api_base_url=os.getenv('MASTODON_API_BASE_URL')
)

class MastodonProxy:
    def __init__(self):
        self.mastodon = mastodon

    def get_latest_toots(self, limit=50):
        toots = self.mastodon.timeline_public(limit=limit)
        return toots

