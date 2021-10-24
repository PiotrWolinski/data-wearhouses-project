import os
from generators.departments import DepartmentGenerator
from generators.clients import ClientGenerator
from generators.consultations import ConsultationGenerator

class MainGenerator:

    def __init__(self):
        self.generators = {}

    def init_generators(self):
        self.generators['departments'] = DepartmentGenerator()
        self.generators['clients'] = ClientGenerator()
        self.generators['consultations'] = ConsultationGenerator()
        
    def start_generators(self):
        for generator in self.generators.values():
            generator.generate()

    def save_to_bulks(self):
        if not os.path.exists('bulks'):
            os.makedirs('bulks')
            
        for generator in self.generators.values():
            generator.save_to_bulk()

if __name__ == '__main__':
    g = MainGenerator()
    g.init_generators()
    g.start_generators()
    g.save_to_bulks()
