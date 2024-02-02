
from domain.toots import Toot
from datetime import timedelta

class TootCollector:
    def __init__(self, mastodon_proxy):
        self.mastodon_proxy = mastodon_proxy

    def collect_latest_toots(self):
        raw_toots = self.mastodon_proxy.get_latest_toots()
        toots = []
        for raw_toot in raw_toots:
            # Asegurarse de que created_at sea "naive" y ajustar la hora
            created_at_adjusted = raw_toot['created_at'].replace(tzinfo=None) + timedelta(hours=1)
            toot = Toot(
                id=raw_toot['id'],
                content=raw_toot['content'],
                username=raw_toot['account']['username'],
                language=raw_toot.get('language', 'unknown'),
                created_at=created_at_adjusted
            )
            toots.append(toot)
        return toots
