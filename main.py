import os
from generators.departments import DepartmentGenerator
from generators.clients import ClientGenerator
from generators.consultants import ConsultantGenerator
from generators.benefits import BenefitGenerator
from generators.consultations import ConsultationGenerator
from generators.rating_types import RatingTypeGenerator
from generators.ratings import RatingGenerator
from generators.surveys import SurveyGenerator

class MainGenerator:

    def __init__(self):
        self.generators = {}
        self._contracts_issue_dates = []

    def init_generators(self):
        self.generators['departments'] = DepartmentGenerator()
        self.generators['clients'] = ClientGenerator()
        self.generators['consultants'] = ConsultantGenerator()
        self.generators['surveys'] = SurveyGenerator()
        self.generators['rating_types'] = RatingTypeGenerator()
        self.generators['ratings'] = RatingGenerator()
        
        # Benefits generator is not with others, because he needs params and is dependant
        self.benefits_generator = BenefitGenerator()
        self.consultations_generator = ConsultationGenerator()
        
    def start_generators(self):
        for generator in self.generators.values():
            generator.generate()

    def save_to_bulks(self):
        if not os.path.exists('bulks'):
            os.makedirs('bulks')
            
        for generator in self.generators.values():
            generator.save_to_bulk()

        self.benefits_generator.save_to_bulk()
        self.consultations_generator.save_to_bulk()

    def generate_benefits(self):
        self._contracts_issue_dates = self.generators['consultants'].generate_employment_dates()
        self.benefits_generator.generate(self._contracts_issue_dates)

    def generate_consultations(self):
        self._contracts_issue_dates = self.generators['consultants'].generate_employment_dates()
        self.consultations_generator.generate(self._contracts_issue_dates)

    def generate_csv(self):
        self.generators['consultants'].export_to_csv()

if __name__ == '__main__':
    g = MainGenerator()
    g.init_generators()
    g.start_generators()
    g.generate_csv()
    g.generate_benefits()
    g.generate_consultations()
    g.save_to_bulks()
