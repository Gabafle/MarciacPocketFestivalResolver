from backend.buildeur.utils import BuilderUtils
from backend.structure.Bodyguard import Bodyguard


class changeBodyGuardServices:
    def __init__(self, party):
        self.party = party

    def change_bodyguard(self, number_bodyguard):
        bodyguard_count = self.party.elements.count(Bodyguard())
        bodyguard_max = Bodyguard().max
        bodyguard_min = Bodyguard().min

        if number_bodyguard < bodyguard_min:
            number_bodyguard = bodyguard_min

        if number_bodyguard > bodyguard_max:
            number_bodyguard = bodyguard_max

        if number_bodyguard > bodyguard_count:
            self.add_bodyguard(number_bodyguard, bodyguard_count)

        if number_bodyguard < bodyguard_count:
            self.remove_bodyguard(number_bodyguard)

    def remove_bodyguard(self, number_chair):
        BuilderUtils(self.party).remove_element(number_chair, Bodyguard)

    def add_bodyguard(self, number_chair, chair_count):
        BuilderUtils(self.party).add_element(number_chair, chair_count, Bodyguard)
