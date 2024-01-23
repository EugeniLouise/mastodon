

import pandas as pd
from proxies.mastodon_proxy import MastodonProxy

def guardar_toots_en_excel(nuevos_toots, nombre_archivo='toots.xlsx'):
    df_existente = pd.read_excel(nombre_archivo)

    # Convertir los nuevos toots en un DataFrame
    data = [{'id': toot['id'], 'Language': toot['language'], 'Username': toot['account']['username'], 'Created at': pd.to_datetime(toot['created_at']).replace(tzinfo=None), 'Content': toot['content']} for toot in nuevos_toots]
    df_nuevos = pd.DataFrame(data)

    # Concatenar los DataFrames existente y nuevos
    df_total = pd.concat([df_existente, df_nuevos], ignore_index=True)

    # Guardar el DataFrame resultante en el archivo Excel
    df_total.to_excel(nombre_archivo, index=False)

# Inicializar la instancia de MastodonProxy
mastodon_proxy = MastodonProxy()

# Obtener nuevos toots
nuevos_toots = mastodon_proxy.get_toot()

# Guardar los nuevos toots en el archivo Excel
guardar_toots_en_excel(nuevos_toots)

print("Nuevos toots agregados a 'toots.xlsx'")


#agafa cada toot que ha trobat (DE RECOLECTED TOOTS) i el guarda en un excel que crea (cada fila un toot, cada columna un atribut).