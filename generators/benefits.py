import random
import codecs
import pathlib
import datetime

class BenefitsGenerator:

    START_ID = 0
    BENEFITS = {
        'Sports Card': {
            'options': ['Multisport', 'FitSport', 'Medicover Sport'],
            'employee_cost': (20, 200),
            'employer_cost': (150, 300) 
        },
        'Lunch Card': {
            'options': ['Edenred Card', 'UpLunch'],
            'employee_cost': (30, 110),
            'employer_cost': (200, 400)
        },
        'Phone': {
            'options': ['iPhone 12 mini', 'Samsung S20', 'Motorola'],
            'employee_cost': (10, 500),
            'employer_cost': (400, 4000)
        },
        'Car': {
            'options': ['Skoda Fabia', 'Toyota Yaris', 'Toyota Prius', 'Skoda Superb'],
            'employee_cost': (300, 1200),
            'emplyer_cost': (3000, 6000)
        },
        'Laptop': {
            'options': ['Macbook Pro 13',' Macbook Air', 'Lenovo Thinkpad'],
            'employee_cost': (10, 100),
            'employer_cost': (200, 400)
        },
        'Holiday Bonus': {
            'options': [ 'Summer Holiday Bonus', 'Weekend Trip Bonus'],
            'employee_cost': (10, 200),
            'employer_cost': (300, 2000)
        },
        'Headphones': {
            'options': ['Sony WH-1000X', 'Microsoft Surface Headphones 2', 'Sennheiser HD 350BT', 'Jabra Evolve 2'],
            'employee_cost': (20, 100),
            'employer_cost': (120, 430)
        }
    }
    CONSULTANTS_AMOUNT = 1500
    BENEFIT_RATE = 0.4
    BENEFIT_FINISHED_CHANCE = 0.1
    class Benefit:

        def __init__(self, id, benefit_name, benefit_type, issue_date, end_date, employer_cost, employee_cost, consultant_id, show_id=False):
            self.id = id
            self.benefit_name = benefit_name
            self.benefit_type = benefit_type
            self.issue_date = issue_date
            self.end_date = end_date
            self.employer_cost = employer_cost
            self.employee_cost = employee_cost
            self.consultant_id = consultant_id
            self._show_id = show_id
            
        def __str__(self):
            id = f'{self.id if self._show_id else ""}'
            s = f'{self.benefit_name}|{self.benefit_type}|{self.issue_date}|{self.employer_cost}|{self.employee_cost}|{self.consultant_fk}'
            return s if id == '' else f'{id}|{s}'

    def __init__(self, contracts_issue_dates=None, consultants_amount=100, start_id=None):
        self._contracts_issue_dates = contracts_issue_dates
        self._current_id = start_id if start_id else self.START_ID
        self._consultants_amount = consultants_amount
        self._benefits = []
 
    @property
    def current_id(self):
        current_id = self._current_id
        self._current_id += 1
        return current_id

    def get_random_date_between(self, contract_start_date, contract_end_date=None):
        first_day = contract_start_date
        last_day = datetime.date(2021, 10, 24) if contract_end_date is not None else contract_end_date

        time_between_dates = last_day - first_day
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = first_day + datetime.timedelta(days=random_number_of_days)

        return random_date

    def generate(self):
        self._benefits = []

        for consultant_id in range(self._consultants_amount):
            benefit = random.uniform(0, 1) < self.BENEFIT_RATE

            if benefit:
                # Contract issue dates must be tuples with (start_date, end_date), ie. (date, None) if end_date is '-'
                current_id = self.current_id
                benefit_type = random.choice(self.BENEFITS.keys())
                benefit_name = random.choice(self.BENEFITS[benefit_type]['options'])
                start_date = self.get_random_date_between(*self._contracts_issue_dates[consultant_id])
                end_date = self.get_random_date_between(start_date, None)
                employee_cost = random.randint(*self.BENEFITS[benefit_type]['employee_cost'])
                employer_cost = random.randint(*self.BENEFITS[benefit_type]['employer_cost'])

                self._benefits.append(self.Benefit(id=current_id,
                                                    benefit_type=benefit_type,
                                                    benefit_name=benefit_name,
                                                    start_date=start_date,
                                                    end_date=end_date,
                                                    employee_cost=employee_cost,
                                                    employer_cost=employer_cost,
                                                    consultant_id=consultant_id))

    def print(self):
        for deparment in self._benefits:
            print(deparment)

    def save_to_bulk(self):
        current_path = pathlib.Path().resolve()

        with codecs.open(f'{current_path}/bulks/benefits.bulk', 'w', 'utf-8') as file:
            for benefit in self._benefits:
                file.write(f'{benefit}\n')
