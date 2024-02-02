

from proxy.mastodon_proxy import MastodonProxy
from uses_cases.toot_collector import TootCollector
from uses_cases.toot_by_language import TootByLanguage
from repository.toot_repository import TootRepository
from repository.language_stats_repository import LanguageStatsRepository

class TootController:
    def __init__(self):
        self.mastodon_proxy = MastodonProxy()
        self.toot_collector = TootCollector(self.mastodon_proxy)
        self.toot_saver = TootRepository()
        self.language_stats_saver = LanguageStatsRepository()

    def run(self):
        toots = self.toot_collector.collect_latest_toots()
        self.toot_saver.save_toots_to_excel(toots)
        language_stats = TootByLanguage(toots).calculate_language_stats()
        self.language_stats_saver.save_language_stats_to_excel(language_stats)
