import time
import random
from mastodon import Mastodon

# Eugenia procura instal·lar la llibreria/module que estem usant executanty això a la terminal
# pip install Mastodon.py --target ./venv/Lib/site-packages

# Initialize Mastodon API
mastodon = Mastodon(
    client_id='qkIKn3ytvhkdNQGMPuRQt14Zw0nKCmTMhWfexRHpWIc',
    client_secret='TkHuLSunv4Y6WZf6HAh_07ZHYHfIIzPdGJtzZWuJeE8',
    access_token='X0FwiBlDTKKo-FUAZ7uc26IE_cPZI1D0tFZMUzrgvP8',
    api_base_url='https://mastodon.social'
)


def get_random_toot():
    # Get public timeline
    toots = mastodon.timeline_public(limit=40)

    # Pick a random toot
    if toots:
        random_toot = random.choice(toots)
        print(f"{random_toot['account']['username']}: {random_toot['content']}")


while True:
    get_random_toot()
    time.sleep(2)
