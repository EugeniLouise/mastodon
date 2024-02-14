from proxy.mastodon_proxy import MastodonProxy
from repository.language_stats_repository import LanguageStatsRepository
from repository.toot_repository import TootRepository
from uses_cases.toot_by_language import TootByLanguage
from uses_cases.toot_collector import TootCollector


class TootController:
    def __init__(self):
        self.mastodon_proxy = MastodonProxy()
        self.toot_collector = TootCollector(self.mastodon_proxy)
        self.toot_repository = TootRepository()
        self.language_stats_repository = LanguageStatsRepository()

    def run(self):
        toots = self.toot_collector.collect_latest_toots()

        # Save toots to excel
        self.toot_repository.save_toots_to_excel(toots)

        # Save toot count by language
        language_stats = TootByLanguage().calculate_language_stats(toots)
        self.language_stats_repository.save_language_stats_to_excel(language_stats)
