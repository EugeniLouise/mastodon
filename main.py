
import time
from proxies.mastodon_proxy import MastodonProxy
import pandas as pd

#Initialize the instance
mastodon = MastodonProxy().mastodon()
toots = MastodonProxy().get_toot() #obtaining toots data

# Preparar los datos para el DataFrame
data = []
for toot in toots:
    id = toot['id']
    language = toot['language']
    username = toot['account']['username']
    content = toot['content']
    created_at = pd.to_datetime(toot['created_at']).replace(tzinfo=None)
    data.append({'id': id, 'Language': language, 'Username': username, 'Created at': created_at, 'Content': content})

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel
df.to_excel('toots.xlsx', index=False)

print("Toots guardados en 'toots.xlsx'")



"""
while True:
    toots = MastodonProxy().get_toot() #obtaining toots data
    # Pick a random toot
    if toots:
        last_toot = toots[-1] #taking last toot
        print(f"{last_toot['account']['username']}: {last_toot['content']}")
    time.sleep(2)
"""