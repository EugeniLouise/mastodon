

from proxies.mastodon_proxy import MastodonProxy

# Orquestador que utiliza MastodonProxy para obtener toots
class Orchestrator:
    def __init__(self, mastodon_proxy):
        self.mastodon_proxy = mastodon_proxy

    def get_recent_toots(self):
        # Llama a MastodonProxy para obtener los toots más recientes
        return self.mastodon_proxy.get_toot()


# Uso del código
mastodon_proxy = MastodonProxy()
toot_orchestrator = Orchestrator(mastodon_proxy)

recent_toots = toot_orchestrator.get_recent_toots()

# Mostrar los toots
for toot in recent_toots:
    print(f"{toot['account']['username']}: {toot['content']}")

"""
1. call api
mastodon_api = MastodonProxy().mastodon()

"""


#clase que crida a totes les altres per nar fent.
#en el main: crida al controller i executa by time sleep.