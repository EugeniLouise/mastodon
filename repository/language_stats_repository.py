import pandas as pd


class LanguageStatsRepository:
    def save_language_stats_to_excel(self, language_stats, filename="language_stats.xlsx"):
        data = [
            {
                'Language': language,
                'Count': stats['count'],
                'Last User': stats['last_user']
            }
            for language, stats in language_stats.items()
        ]
        df_language_stats = pd.DataFrame(data)

        try:
            df_language_stats.to_excel(filename, index=False)
            print(f"Estadísticas guardadas exitosamente en {filename}.")
        except Exception as e:
            print(f"Error al guardar las estadísticas en {filename}: {e}")
