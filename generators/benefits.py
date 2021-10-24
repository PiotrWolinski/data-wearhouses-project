import random
import codecs
import pathlib

class BenefitGenerator:

    START_ID = 0
    BENEFIT_NAME = ['Multisport', 'Lunch Card', 'Phone', 'Car', 'Laptop', 'Holiday Bonus', 'Headphones']

    class Benefit:

        def __init__(self, id, street, building_number, city, postal_code, consultants, call_center, show_id=False):
            self.id = id
            self.street = street
            self.building_number = building_number
            self.city = city
            self.postal_code = postal_code
            self.consultants = consultants
            self.call_center = call_center
            self._show_id = show_id

        def __str__(self):
            id = f'{self.id if self._show_id else ""}'
            s = f'{self.street}|{self.building_number}|{self.city}|{self.postal_code}|{self.consultants}|{self.call_center}'
            return s if id == '' else f'{id}|{s}'

    def __init__(self, benefits_amount=15, start_id=None):
        self._current_id = start_id if start_id else self.START_ID
        self._benefits_amount = benefits_amount
        self._benefits = []

    @property
    def current_id(self):
        current_id = self._current_id
        self._current_id += 1
        return current_id

    def generate(self):
        self._benefits = []

        for _ in range(self._benefits_amount):
            current_id = self.current_id
            street = random.choice(self.STREETS)
            building_number = random.randint(*self.BUILDING_NUMBER_RANGE)
            city = random.choice(self.CITIES)
            postal_code = f'{random.randint(0,9)}{random.randint(0,9)}-{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
            consultants_amount = random.randint(*self.CONSULTANTS_RANGE)
            call_center = True if random.uniform(0, 1) < self.CALL_CENTER_RATE else False

            self._benefits.append(self.Benefit(id=current_id,
                                                street=street,
                                                building_number=building_number,
                                                city=city,
                                                postal_code=postal_code,
                                                consultants=consultants_amount,
                                                call_center=call_center))

    def print(self):
        for deparment in self._benefits:
            print(deparment)

    def save_to_bulk(self):
        current_path = pathlib.Path().resolve()

        with codecs.open(f'{current_path}/bulks/benefits.bulk', 'w', 'utf-8') as file:
            for benefit in self._benefits:
                file.write(f'{benefit}\n')
