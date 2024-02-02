

import pandas as pd

class LanguageStatsRepository:
    def save_language_stats_to_excel(self, language_stats, filename="language_stats.xlsx"):
        df = pd.DataFrame([{'Language': language, 'Count': stats['count'], 'Last User': stats['last_user']} for language, stats in language_stats.items()])
        df.to_excel(filename, index=False)