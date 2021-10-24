import pandas
import random
import codecs
import pathlib
    
class ClientGenerator:

    START_ID = 0

    class Client:

        def __init__(self, id, name, surname, show_id=False):
            self.id = id
            self.name = name
            self.surname = surname
            self._show_id = show_id
        
        def __str__(self):
            id = f'{self.id if self._show_id else ""}'
            s = f'{self.name}|{self.surname}'
            return s if id == '' else f'{id}|{s}'

    def __init__(self, clients_amount=100_000, start_id=None):
        self._current_id = start_id if start_id else self.START_ID
        self._clients_amount = clients_amount
        self._clients = []
        self._names = []
        self._surnames = []
        self.read_names()
        self.read_surnames()

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
        self._clients = []

        for _ in range(self._clients_amount):
            current_id = self.current_id
            name = random.choice(self._names)
            surname = random.choice(self._surnames)

            self._clients.append(self.Client(id=current_id,
                                        name=name,
                                        surname=surname))
            

    def print(self):
        for client in self._clients:
            print(client)
    
    def save_to_bulk(self):
        current_path = pathlib.Path().resolve()

        with codecs.open(f'{current_path}/bulks/clients.bulk', 'w', 'utf-8-sig') as file:
            for client in self._clients:
                file.write(f'{client}\n')
