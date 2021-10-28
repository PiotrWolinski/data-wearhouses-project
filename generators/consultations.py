import random
import codecs
import pathlib
import datetime
    
class ConsultationGenerator:

    START_ID = 0
    CONSULTANTS_ID_RANGE = (1, 1500)
    CLIENTS_ID_RANGE = (1, 100_000)
    FIRST_DAY = datetime.date(2020, 10, 24)
    TOPICS = ["technical issue", "offer question", "feedback"]
    TOPICS_WEIGHTS = [0.1, 0.8, 0.1]
    class Consultation:

        def __init__(self, id, consultant, client, start_time, end_time, topic, show_id=False):
            self.id = id
            self.consultant = consultant
            self.client = client
            self.start_time = start_time
            self.end_time = end_time
            self.topic = topic
            self._show_id = show_id
        
        def __str__(self):
            id = f'{self.id if self._show_id else ""}'
            s = f'{self.consultant}|{self.client}|{self.start_time}|{self.end_time}|{self.topic}'
            return s if id == '' else f'{id}|{s}'
    
    def __init__(self, consultations_amount=1_000_000, start_id=None):
        self._current_id = start_id if start_id else self.START_ID
        self._consultations_amount = consultations_amount
        self._consultations = []
    
    @property
    def current_id(self):
        current_id = self._current_id
        self._current_id += 1
        return current_id

    def generate(self, contracts_issue_dates=None):
        self._contracts_issue_dates = contracts_issue_dates
        self._consultations = []

        for _ in range(self._consultations_amount):
            current_id = self.current_id
            consultant = -1
            while consultant == -1:
                random_consultant = random.randint(*self.CONSULTANTS_ID_RANGE)
                if self._contracts_issue_dates[random_consultant - 1][1] == '-':
                    consultant = random_consultant
                elif self._contracts_issue_dates[random_consultant - 1][1] > self.FIRST_DAY:
                    chance = (self._contracts_issue_dates[random_consultant - 1][1] - self.FIRST_DAY).days / 360
                    if random.uniform(0, 1) < chance:
                        consultant = random_consultant
            client = random.randint(*self.CLIENTS_ID_RANGE)
            day = self.get_random_date_between(self.FIRST_DAY, self._contracts_issue_dates[consultant - 1][1])
            time_in_day = datetime.time(random.randrange(8) + 8, random.randrange(60), random.randrange(60))
            start_time = datetime.datetime.combine(day, time_in_day)
            consultation_time = datetime.timedelta(minutes = random.randrange(60), seconds = random.randrange(60))
            end_time = start_time + consultation_time
            topic = random.choices(self.TOPICS, self.TOPICS_WEIGHTS)[0]

            self._consultations.append(self.Consultation(id=current_id,
                                                         consultant=consultant,
                                                         client=client,
                                                         start_time=start_time,
                                                         end_time=end_time,
                                                         topic=topic))
            
    def get_random_date_between(self, _first_day, _last_day):
        first_day = _first_day
        last_day =  _last_day if type(_last_day) == datetime.date else datetime.date(2021, 10, 24)

        time_between_dates = last_day - first_day
        days_between_dates =  time_between_dates.days if int(time_between_dates.days) > 0 else 1

        random_number_of_days = random.randrange(days_between_dates)
        random_date = first_day + datetime.timedelta(days=random_number_of_days)

        return random_date

    def print(self):
        for consultation in self._consultations:
            print(consultation)
    
    def save_to_bulk(self):
        current_path = pathlib.Path().resolve()

        with codecs.open(f'{current_path}/bulks/consultations.bulk', 'w', 'utf-8-sig') as file:
            for consultation in self._consultations:
                file.write(f'{consultation}\n')
