import os

import pandas as pd


class TootRepository:
    def save_toots_to_excel(self, toots, filename="toots.xlsx"):
        data = [  # TODO: què conté data??
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
                df.to_excel(filename, index=False)
                print(f"Data added to existing file {filename}.")

            except Exception as e:  # TODO: classificar comportaments segons tipus d'excepció
                print(f"Error adding data to existing file: {e}")

        else:
            try:
                df = new_toots_df
                print(f"Data added to file {filename}.")
                df.to_excel(filename, index=False)

            except Exception as e:
                print(f"Error al crear el archivo {filename}: {e}")

    def save_toots_to_excel_guilli(self, toots, filename="toots.xlsx"):
        data = [  # TODO: què conté data??
            {
                'ID': toot.id,
                'Language': toot.language,
                'Username': toot.username,
                'Created At': toot.created_at,
                'Content': toot.content
            }
            for toot in toots]

        new_toots_df = pd.DataFrame(data)

        try:
            if os.path.exists(filename):
                existing_toots_df = pd.read_excel(filename)
                new_toots_df = pd.concat([existing_toots_df, new_toots_df], ignore_index=True)
            new_toots_df.to_excel(filename, index=False)
            print(f"Data added to file {filename}.")

        except Exception as e:
            print(f"Error adding data to file: {e}")
