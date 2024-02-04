import os

from dotenv import load_dotenv
from mastodon import Mastodon

# Load environment variables from a .env file to Python environment variables
load_dotenv(dotenv_path='C:/Users/Eugenia Subirons/PycharmProjects/Mastodon_G/proxy/credentials.env')


class MastodonProxy:
    def __init__(self):
        self.mastodon = Mastodon(
            client_id=os.getenv('MASTODON_CLIENT_ID'),
            client_secret=os.getenv('MASTODON_CLIENT_SECRET'),
            access_token=os.getenv('MASTODON_ACCESS_TOKEN'),
            api_base_url=os.getenv('MASTODON_API_BASE_URL')
        )

    def get_latest_toots(self, limit=50):
        toots = self.mastodon.timeline_public(limit=limit)
        return toots
