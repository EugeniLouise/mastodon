from proxy.mastodon_proxy import MastodonProxy
from repository.language_stats_repository import LanguageStatsRepository
from repository.toot_repository import TootRepository
from uses_cases.toot_by_language import TootByLanguage
from uses_cases.toot_collector import TootCollector


class TootController:
    def __init__(self):
        self.mastodon_proxy = MastodonProxy()
        self.toot_collector = TootCollector(self.mastodon_proxy)
        self.toot_saver = TootRepository()  # TODO: renombrar variable para no confundir
        self.language_stats_saver = LanguageStatsRepository() # TODO: renombrar variable para no confundir

    def run(self):
        toots = self.toot_collector.collect_latest_toots()

        # Save toots to excel
        self.toot_saver.save_toots_to_excel(toots)

        # Save toot count by language
        language_stats = TootByLanguage(toots).calculate_language_stats()
        self.language_stats_saver.save_language_stats_to_excel(language_stats)
