import random
import codecs
import pathlib

class SurveyGenerator:

    START_ID = 1
    REWARD_AVAILABLE_RATE = 0.05
    RATINGS = [1, 2, 3, 4, 5]
    RATINGS_WEIGHTS = [0.05, 0.2, 0.35, 0.3, 0.1]
    SURVEYS_AMOUNT = 600_000

    class Survey:

        def __init__(self, id, reward_available, consultation, overall_rating, show_id=True):
            self.id = id
            self.reward_available = reward_available
            self.consultation = consultation
            self.overall_rating = overall_rating
            self._show_id = show_id

        def __str__(self):
            id = f'{self.id if self._show_id else ""}'
            s = f'{self.reward_available}|{self.consultation}|{self.overall_rating}'
            return s if id == '' else f'{id}|{s}'

    def __init__(self, surveys_amount=SURVEYS_AMOUNT, start_id=None):
        self._current_id = start_id if start_id else self.START_ID
        self._surveys_amount = surveys_amount
        self._surveys = []

    @property
    def current_id(self):
        current_id = self._current_id
        self._current_id += 1
        return current_id

    def generate(self):
        self._surveys = []

        for i in range(self._surveys_amount):
            current_id = self.current_id
            reward_available = True if random.uniform(0, 1) < self.REWARD_AVAILABLE_RATE else False
            consultation = i+1
            overall_rating = random.choices(self.RATINGS, self.RATINGS_WEIGHTS)[0]

            self._surveys.append(self.Survey(id=current_id,
                                                 reward_available=int(reward_available),
                                                 consultation=consultation,
                                                 overall_rating=overall_rating))

    def print(self):
        for survey in self._surveys:
            print(survey)

    def save_to_bulk(self):
        current_path = pathlib.Path().resolve()

        with codecs.open(f'{current_path}/bulks/surveys.bulk', 'w', 'utf-8') as file:
            for survey in self._surveys:
                file.write(f'{survey}\n')
