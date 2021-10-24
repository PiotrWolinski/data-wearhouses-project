import random
import codecs
import pathlib
import datetime
    
class ConsultationGenerator:

    START_ID = 0
    CONSULTANTS_ID_RANGE = (1, 1500)
    CLIENTS_ID_RANGE = (1, 100_000)
    FIRST_DAY = datetime.datetime(2020, 10, 24, 8, 0, 0, 0)
    LAST_DAY = datetime.datetime(2021, 10, 24, 8, 0, 0, 0)
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

    def generate(self):
        self._consultations = []

        for _ in range(self._consultations_amount):
            current_id = self.current_id
            consultant = random.randint(*self.CONSULTANTS_ID_RANGE)
            client = random.randint(*self.CLIENTS_ID_RANGE)
            time_in_day = datetime.timedelta(hours = random.randrange(8), minutes = random.randrange(60), seconds = random.randrange(60))
            days_from_start = datetime.timedelta(days = random.randrange((self.LAST_DAY - self.FIRST_DAY).days))
            start_time = self.FIRST_DAY + days_from_start + time_in_day
            consultation_time = datetime.timedelta(minutes = random.randrange(60), seconds = random.randrange(60))
            end_time = start_time + consultation_time
            topic = random.choices(self.TOPICS, self.TOPICS_WEIGHTS)[0]

            self._consultations.append(self.Consultation(id=current_id,
                                                         consultant=consultant,
                                                         client=client,
                                                         start_time=start_time,
                                                         end_time=end_time,
                                                         topic=topic))
            
    def print(self):
        for consultation in self._consultations:
            print(consultation)
    
    def save_to_bulk(self):
        current_path = pathlib.Path().resolve()

        with codecs.open(f'{current_path}/bulks/consultations.bulk', 'w', 'utf-8-sig') as file:
            for consultation in self._consultations:
                file.write(f'{consultation}\n')
