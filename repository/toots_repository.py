import pandas as pd
from proxies.mastodon_proxy import MastodonProxy

class TootSaver:
    def __init__(self, filename='toots_historical.xlsx'):
        self.filename = filename
        self.mastodon_proxy = MastodonProxy()
        self.last_toot_user_by_language = {}
        self.new_toots_count_by_language = {}

    def save_toots_to_excel(self):
        new_toots = self.mastodon_proxy.get_toot() # Get new toots

        try:
            existing_df = pd.read_excel(self.filename)
        except FileNotFoundError:
            existing_df = pd.DataFrame()

        # Convert new toots to a DataFrame and count them by language
        data = []
        self.new_toots_count_by_language.clear()
        for toot in new_toots:
            language = toot['language']
            data.append({'id': toot['id'], 'Language': language, 'Username': toot['account']['username'], 'Created at': pd.to_datetime(toot['created_at']).replace(tzinfo=None), 'Content': toot['content']})
            self.last_toot_user_by_language[language] = toot['account']['username']
            self.new_toots_count_by_language[language] = self.new_toots_count_by_language.get(language, 0) + 1
        new_df = pd.DataFrame(data)

        # Concatenate existing and new DataFrames
        total_df = pd.concat([existing_df, new_df], ignore_index=True)

        # Save the resulting DataFrame to the Excel file
        total_df.to_excel(self.filename, index=False)

    def create_language_statistics_excel(self, stats_filename='toots_language_stats.xlsx'):
        df = pd.read_excel(self.filename)
        language_stats = df.groupby('Language').size().reset_index(name='Total Toots')

        # Add the new toots count column
        language_stats['New Toots Count'] = language_stats['Language'].apply(lambda x: self.new_toots_count_by_language.get(x, 0))

        # Add the last user column
        language_stats['Last User'] = language_stats['Language'].apply(lambda x: self.last_toot_user_by_language.get(x, None))

        # Calculate totals
        total_toots_sum = language_stats['Total Toots'].sum()
        new_toots_sum = language_stats['New Toots Count'].sum()
        totals_row = pd.DataFrame([{'Language': 'Total', 'Total Toots': total_toots_sum, 'New Toots Count': new_toots_sum, 'Last User': ''}])

        # Concatenate the totals row
        language_stats = pd.concat([language_stats, totals_row], ignore_index=True)

        # Save the stats DataFrame to an Excel file
        language_stats.to_excel(stats_filename, index=False)

# Using the class
toot_saver = TootSaver()
toot_saver.save_toots_to_excel()
toot_saver.create_language_statistics_excel()
print("Language statistics added to 'toots_language_stats.xlsx'")
