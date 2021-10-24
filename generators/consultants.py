import pandas 
import random
import codecs
import pathlib
import csv
import datetime
    
class ConsultantGenerator:

    START_ID = 0
    DEPARTMENTS_AMOUNT = 15
    EDUCATION = ['None', 'Bachelor', 'Master', 'Primary', 'Secondary']
    POSITION = ['Assistant', 'Representative', 'IT Support', 'Office assistant', 'Director', 'Receptionist', 'Support assistant', 'Staff assistant', 'Analyst', 'Copywriter']
    POSITION_WEIGHTS = [0.08,   0.1,                0.1,           0.15,           0.01,           0.09,            0.1,               0.15,           0.12,       0.1]
    EMPLOYMENT_RATE = 0.9
    CONSULTANTS_AMOUNT = 1500
    TOTAL_WORKERS = 5000

    def __init__(self, consultants_amount=1500, start_id=None):
        self._current_id = start_id if start_id else self.START_ID
        self._consultants_amount = consultants_amount
        self._consultants = []
        self._names = []
        self._surnames = []
        self._total_workers = consultants_amount + 3500
        self.read_names()
        self.read_surnames()

    class Consultant:

        def __init__(self, id, department, name, surname, show_id=False):
            self.id = id
            self.department = department
            self.name = name
            self.surname = surname
            self._show_id = show_id

        def to_list(self):
            arr = []
            arr.append(self.id)
            arr.append(self.department)
            arr.append(self.name)
            arr.append(self.surname)

            return arr
        
        def __str__(self):
            id = f'{self.id if self._show_id else ""}'
            s = f'{self.department}|{self.name}|{self.surname}'
            return s if id == '' else f'{id}|{s}'

    def read_names(self):
        names_df = pandas.read_csv("names.csv")
        self._names = pandas.Series(names_df.iloc[:, 2].array).array

    def read_surnames(self):
        surnames_df = pandas.read_csv("surnames.csv")
        self._surnames = pandas.Series(surnames_df.iloc[:, 0].array).astype(str).array
        self._surnames = [surname[0] + surname[1:].lower() for surname in self._surnames]
    
    @property
    def current_id(self):
        current_id = self._current_id
        self._current_id += 1
        return current_id

    def generate(self):
        self._consultants = []

        for _ in range(self._consultants_amount):
            current_id = self.current_id
            department = random.randint(0, self.DEPARTMENTS_AMOUNT)
            name = random.choice(self._names)
            surname = random.choice(self._surnames)

            self._consultants.append(self.Consultant(id=current_id,
                                        department=department,
                                        name=name,
                                        surname=surname))
            
    def print(self):
        for consultant in self._consultants:
            print(consultant)
    
    def save_to_bulk(self):
        current_path = pathlib.Path().resolve()

        with codecs.open(f'{current_path}/bulks/consultants.bulk', 'w', 'utf-8-sig') as file:
            for consultant in self._consultants:
                file.write(f'{consultant}\n')

    def export_to_csv(self):

        def get_random_birth_date():
            first_day = datetime.date(1950, 1, 1)
            last_day = datetime.date(2000, 12, 31)

            time_between_dates = last_day - first_day
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date = first_day + datetime.timedelta(days=random_number_of_days)

            return random_date

        def get_random_sign_date():
            first_day = datetime.date(2005, 10, 24)
            last_day = datetime.date(2021, 10, 24)

            time_between_dates = last_day - first_day
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date = first_day + datetime.timedelta(days=random_number_of_days)

            return random_date

        def define_employment(start_date):
            fired = True if random.uniform(0, 1) > self.EMPLOYMENT_RATE else False

            if fired and (datetime.date(2021, 10, 24) - start_date).days > 30:
                correct_date = False
                end_date = start_date

                while not correct_date:
                    end_date = get_random_sign_date()

                    working_days = (end_date - start_date).days

                    if working_days > 30:
                        correct_date = True

                return end_date

            return '-'

        with open('ceo_excel.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',')

            for consultant in self._consultants:
                consultant_arr = consultant.to_list()
                consultant_arr.append(get_random_birth_date())
                consultant_arr.append(random.choice(self.EDUCATION))
                consultant_arr.append('Consultant')
                consultant_arr.append(random.uniform(4000, 7000))
                consultant_arr.append(get_random_sign_date())
                consultant_arr.append(define_employment(consultant_arr[-1]))
                writer.writerow(consultant_arr)

            for _ in range(self._total_workers - self._consultants_amount):
                employee_arr = []
                employee_arr.append(self.current_id)
                employee_arr.append(random.randint(0, self.DEPARTMENTS_AMOUNT))
                employee_arr.append(random.choice(self._names))
                employee_arr.append(random.choice(self._surnames))
                employee_arr.append(get_random_birth_date())
                employee_arr.append(random.choice(self.EDUCATION))
                employee_arr.append(random.choices(self.POSITION, self.POSITION_WEIGHTS)[0])
                employee_arr.append(random.uniform(4000, 7000))
                employee_arr.append(get_random_sign_date())
                employee_arr.append(define_employment(employee_arr[-1]))
                writer.writerow(employee_arr)
