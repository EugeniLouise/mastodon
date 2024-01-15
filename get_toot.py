

from mastodon_api import MastodonApi
mastodon = MastodonApi().mastodon() #aqui estoy duplicando codigo, pq ya lo tengo en mastodon_api...

# Get toot from public timeline class
class GetToot:
    def get_toot(self):
        toots = mastodon.timeline_public(limit=40)
        return toots
