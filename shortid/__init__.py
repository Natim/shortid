import base64
import os
import random


def shortid(nb_bytes=6):
    return base64.urlsafe_b64encode(
        os.urandom(nb_bytes)).decode('utf-8').rstrip('=')


class ShortId(object):
    # From 7 to 14 characters: Up to 64^7 + 64^8 + ... + 64^14
    def __init__(self, min_bytes=5, max_bytes=10):
        self.min_bytes = min_bytes
        self.max_bytes = max_bytes

    def generate(self, nb_bytes=None):
        if not nb_bytes:
            random.seed = os.urandom(1024)
            nb_bytes = random.randint(self.min_bytes, self.max_bytes)
        return shortid(nb_bytes)
