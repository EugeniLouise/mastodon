
import time
import random
from mastodon_api import MastodonApi #Mastodon API conection class
from get_toot import GetToot # Get toot from public timeline class

#Initialize the instance
mastodon = MastodonApi().mastodon()

while True:
    toots = GetToot().get_toot() #obtaining toots data

    # Pick a random toot
    if toots:
        last_toot = toots[-1] #taking last toot
        print(f"{last_toot['account']['username']}: {last_toot['content']}")
    time.sleep(2)
