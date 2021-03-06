import random
import codecs
import pathlib

class RatingGenerator:

    START_ID = 1
    RATING_TYPES = ["consultant rating", "solution rating"]
    RATINGS = [1, 2, 3, 4, 5]
    RATING_WEIGHTS = {
        "consultant rating": [0.05, 0.15, 0.4, 0.35, 0.05],
        "solution rating": [0.2, 0.1, 0.3, 0.2, 0.2]
    }
    RATINGS_AMOUNT = 600_000

    class Rating:

        def __init__(self, id, survey, rating_type, rating_value, show_id=True):
            self.id = id
            self.survey = survey
            self.rating_type = rating_type
            self.rating_value = rating_value
            self._show_id = show_id

        def __str__(self):
            id = f'{self.id if self._show_id else ""}'
            s = f'{self.survey}|{self.rating_type}|{self.rating_value}'
            return s if id == '' else f'{id}|{s}'

    def __init__(self, surveys_amount=RATINGS_AMOUNT, start_id=None):
        self._current_id = start_id if start_id else self.START_ID
        self._surveys_amount = surveys_amount
        self._ratings = []

    @property
    def current_id(self):
        current_id = self._current_id
        self._current_id += 1
        return current_id

    def generate(self):
        self._ratings = []

        for i in range(self._surveys_amount):
            current_id = self.current_id
            survey = i+1

            for type in self.RATING_TYPES:
                rating_value = random.choices(self.RATINGS, self.RATING_WEIGHTS[type])[0]
                self._ratings.append(self.Rating(id=current_id,
                                                survey=survey,
                                                rating_type=type,
                                                rating_value=rating_value))

    def print(self):
        for rating in self._ratings:
            print(rating)

    def save_to_bulk(self):
        current_path = pathlib.Path().resolve()

        with codecs.open(f'{current_path}/bulks/ratings.bulk', 'w', 'utf-8') as file:
            for rating in self._ratings:
                file.write(f'{rating}\n')
