


class GettintToots:
    def __init__(self, mastodon_proxy):
        self.mastodon_proxy = mastodon_proxy

    def getting_recent_toots(self):
        return self.mastodon_proxy.get_toot()

# recolecta tots els ultims 5 toots i guardar els atribut que ens interessen (descrits al init del domain).

