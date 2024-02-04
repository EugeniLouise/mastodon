class TootByLanguage:
    def __init__(self, toots):
        self.toots = toots

    def calculate_language_stats(self):
        language_stats = {}
        for toot in self.toots:
            if toot.language not in language_stats:
                language_stats[toot.language] = {'count': 0, 'last_user': ''}
            language_stats[toot.language]['count'] += 1
            language_stats[toot.language]['last_user'] = toot.username
        return language_stats
