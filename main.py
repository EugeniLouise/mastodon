
import time
from proxies.mastodon_proxy import MastodonProxy

#Initialize the instance
mastodon = MastodonProxy().mastodon()

while True:
    toots = MastodonProxy().get_toot() #obtaining toots data

    # Pick a random toot
    if toots:
        last_toot = toots[-1] #taking last toot
        print(f"{last_toot['account']['username']}: {last_toot['content']}")
    time.sleep(2)
