

import pandas as pd
from proxies.mastodon_proxy import MastodonProxy

class TootSaver:
    def __init__(self, filename='toots.xlsx'):
        self.filename = filename
        self.mastodon_proxy = MastodonProxy()

    def save_toots_to_excel(self):
        new_toots = self.mastodon_proxy.get_toot() # Get new toots

        try:
            existing_df = pd.read_excel(self.filename)
        except FileNotFoundError:
            existing_df = pd.DataFrame()

        # Convert new toots to a DataFrame
        data = [{'id': toot['id'], 'Language': toot['language'], 'Username': toot['account']['username'], 'Created at': pd.to_datetime(toot['created_at']).replace(tzinfo=None), 'Content': toot['content']} for toot in new_toots]
        new_df = pd.DataFrame(data)

        # Concatenate existing and new DataFrames
        total_df = pd.concat([existing_df, new_df], ignore_index=True)

        # Save the resulting DataFrame to the Excel file
        total_df.to_excel(self.filename, index=False)

# Using the class
toot_saver = TootSaver()
toot_saver.save_toots_to_excel()
print("New toots added to 'toots.xlsx'")


#agafa cada toot que ha trobat (DE RECOLECTED TOOTS) i el guarda en un excel que crea (cada fila un toot, cada columna un atribut).