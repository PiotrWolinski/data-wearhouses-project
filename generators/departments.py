import random
import codecs
import pathlib

class DepartmentGenerator:

    START_ID = 1
    BUILDING_NUMBER_RANGE = (1, 100)
    CITIES = ['Gdańsk', 'Sopot', 'Gdynia', 'Elbląg', 'Poznań', 'Suchy Las', 'Wrocław', 'Warszawa', 'Kraków']
    STREETS = ['Marszałkowska', 'Grunwaldzka', 'Krótka', 'Mickiewicza', 'Jasna', 'Ciemna', 'Wesoła', 'Słoneczna', 'Deszczowa', 'Długa', 'Bałtycka', 'Ratajczaka']
    CALL_CENTER_RATE = 0.9
    class Department:

        def __init__(self, id, street, building_number, city, postal_code, call_center, show_id=True):
            self.id = id
            self.street = street
            self.building_number = building_number
            self.city = city
            self.postal_code = postal_code
            self.call_center = call_center
            self._show_id = show_id

        def __str__(self):
            id = f'{self.id if self._show_id else ""}'
            s = f'{self.street}|{self.building_number}|{self.city}|{self.postal_code}|{self.call_center}'
            return s if id == '' else f'{id}|{s}'

    def __init__(self, departments_amount=15, start_id=None):
        self._current_id = start_id if start_id else self.START_ID
        self._departments_amount = departments_amount
        self._departments = []

    @property
    def current_id(self):
        current_id = self._current_id
        self._current_id += 1
        return current_id

    def generate(self):
        self._departments = []

        for _ in range(self._departments_amount):
            current_id = self.current_id
            street = random.choice(self.STREETS)
            building_number = random.randint(*self.BUILDING_NUMBER_RANGE)
            city = random.choice(self.CITIES)
            postal_code = f'{random.randint(0,9)}{random.randint(0,9)}-{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
            call_center = '1' if random.uniform(0, 1) < self.CALL_CENTER_RATE else '0'

            self._departments.append(self.Department(id=current_id,
                                                street=street,
                                                building_number=building_number,
                                                city=city,
                                                postal_code=postal_code,
                                                call_center=call_center))

    def print(self):
        for deparment in self._departments:
            print(deparment)

    def save_to_bulk(self):
        current_path = pathlib.Path().resolve()

        with codecs.open(f'{current_path}/bulks/departments.bulk', 'w', 'utf-8') as file:
            for department in self._departments:
                file.write(f'{department}\n')
