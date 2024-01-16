
import time
from mastodon_api import MastodonApi

#Initialize the instance
mastodon = MastodonApi().mastodon()

while True:
    toots = MastodonApi().get_toot() #obtaining toots data

    # Pick a random toot
    if toots:
        last_toot = toots[-1] #taking last toot
        print(f"{last_toot['account']['username']}: {last_toot['content']}")
    time.sleep(2)
