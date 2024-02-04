import os

import pandas as pd


class TootRepository:
    def save_toots_to_excel(self, toots, filename="toots.xlsx"):
        data = [
            {
                'ID': toot.id,
                'Language': toot.language,
                'Username': toot.username,
                'Created At': toot.created_at,
                'Content': toot.content
            }
            for toot in toots]

        new_toots_df = pd.DataFrame(data)

        if os.path.exists(filename):
            try:
                existing_toots_df = pd.read_excel(filename)
                df = pd.concat([existing_toots_df, new_toots_df], ignore_index=True)
            except Exception as e:
                print(f"Error al agregar datos al archivo existente: {e}")

        else:
            df = new_toots_df

        df.to_excel(filename, index=False)
