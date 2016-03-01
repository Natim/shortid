import base64
import os
import random


def shortid(nb_char=8):
    nb_bytes = int((nb_char / 4 + 1) * 3)
    return base64.urlsafe_b64encode(
        os.urandom(nb_bytes)).decode('utf-8').rstrip('=')[:nb_char]


class ShortId(object):
    # From 7 to 14 characters: Up to 64^7 + 64^8 + ... + 64^14
    def __init__(self, min_char=7, max_char=14):
        self.min_char = min_char
        self.max_char = max_char

    def generate(self, nb_char=None):
        if not nb_char:
            random.seed = os.urandom(1024)
            nb_char = random.randint(self.min_char, self.max_char)
        return shortid(nb_char)
