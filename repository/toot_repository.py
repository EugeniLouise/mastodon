import os

import pandas as pd


class TootRepository:
    def save_toots_to_excel(self, toots, filename="toots.xlsx"):
        new_df = pd.DataFrame([{
            'ID': toot.id,
            'Language': toot.language,
            'Username': toot.username,
            'Created At': toot.created_at,
            'Content': toot.content
        } for toot in toots])

        if os.path.exists(filename):
            existing_df = pd.read_excel(filename)
            df = pd.concat([existing_df, new_df], ignore_index=True)
        else:
            df = new_df

        df.to_excel(filename, index=False)
