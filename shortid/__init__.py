import base64
import os

# Should change every year with VERSION
# TODO: Automate it
VERSION = 3


def shortid(nb_bytes=6):
    return base64.urlsafe_b64encode(
        os.urandom(nb_bytes)).decode('utf-8').rstrip('=')


class ShortId(object):
    def __init__(self, nb_bytes=6):
        self.nb_bytes = nb_bytes

    def generate(self):
        return shortid(self.nb_bytes)
