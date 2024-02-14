import os

import pandas as pd


class TootRepository:
    def save_toots_to_excel(self, toots, filename="toots.xlsx"):
        toots_parameters = [
            {
                'ID': toot.id,
                'Language': toot.language,
                'Username': toot.username,
                'Created At': toot.created_at,
                'Content': toot.content
            }
            for toot in toots]

        new_toots_df = pd.DataFrame(toots_parameters)
        # Evitar els if/elif/else modificant el codi

        try:
            if os.path.exists(filename):
                existing_toots_df = pd.read_excel(filename)
                new_toots_df = pd.concat([existing_toots_df, new_toots_df], ignore_index=True)
            new_toots_df.to_excel(filename, index=False)
            print(f"Data added to file {filename}.")

        except FileExistsError as fee:
            print(f"Error with file existence: {fee}")

        except ExcelReadError as ere:
            print(f"Error reading excel: {ere}")

        except DataFrameConcatError as dfce:
            print(f"Error with dataframe concat: {dfce}")

        except ExcelWriteError as ewe:
            print(f"Error writing data to Excel file {filename}: {ewe}")

        except Exception as e: # Excepción genérica
            print(f"Error adding data to file: {e}")
