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
                print(f"Data added to existing file {filename}.")
            except Exception as e:
                print(f"Error adding data to existing file: {e}")

        else:
            try:
                df = new_toots_df
                print(f"Data added to file {filename}.")
            except Exception as e:
                print(f"Error al crear el archivo {filename}: {e}")

        df.to_excel(filename, index=False)
