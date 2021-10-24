import random

class Department:

    def __init__(self, id, street, building_number, city, postal_code, consultants, call_center):
        self.id = id
        self.street = street
        self.building_number = building_number
        self.city = city
        self.postal_code = postal_code
        self.consultants = consultants
        self.call_center = call_center

    def __str__(self):
        

class DepartmentGenerator:

    START_ID = 0
    BUILDING_NUMBER_RANGE = (1, 100)
    CITIES = ['Gdańsk', 'Sopot', 'Gdynia', 'Elbląg', 'Poznań', 'Suchy Las', 'Wrocław', 'Warszawa', 'Kraków']
    STREETS = ['Marszałkowska', 'Grunwaldzka', 'Krótka', 'Mickiewicza', 'Jasna', 'Ciemna', 'Wesoła', 'Słoneczna', 'Deszczowa', 'Długa', 'Bałtycka', 'Ratajczaka']
    CONSULTANTS_RANGE = (40, 60)
    CALL_CENTER_RATE = 0.9

    def __init__(self, departments_amount=15, start_id=None):
        _current_id = start_id if start_id else self.START_ID
        _departments_amount = departments_amount
        _departments = []

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
            postal_code = f'{random.randint(9)}{random.randint(9)}-{random.randint(9)}{random.randint(9)}{random.randint(9)}'
            consultants_amount = random.randint(*self.CONSULTANTS_RANGE)
            call_center = True if random.uniform(0, 1) < self.CALL_CENTER_RATE else False

            self._departments.append(Department(id=current_id,
                                                street=street,
                                                building_number=building_number,
                                                city=city,
                                                postal_code=postal_code,
                                                consultants=consultants_amount,
                                                call_center=call_center))

        