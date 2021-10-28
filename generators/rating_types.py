import codecs
import pathlib

class RatingTypeGenerator:

    START_ID = 0
    RATING_TYPES = ["consultant rating", "solution rating"]

    class RatingType:

        def __init__(self, name):
            self.name = name

        def __str__(self):
            s = f'{self.name}'
            return s

    def __init__(self):
        self._rating_types = []

    def generate(self):
        self._rating_types = []

        for rating_type in self.RATING_TYPES:

            self._rating_types.append(self.RatingType(rating_type))

    def print(self):
        for rating_type in self._rating_types:
            print(rating_type)

    def save_to_bulk(self):
        current_path = pathlib.Path().resolve()

        with codecs.open(f'{current_path}/bulks/rating_types.bulk', 'w', 'utf-8') as file:
            for rating_type in self._rating_types:
                file.write(f'{rating_type}\n')
