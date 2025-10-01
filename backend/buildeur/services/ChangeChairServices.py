from backend.buildeur.utils import BuilderUtils
from backend.structure.Chair import Chair


class changeChairService:

    def __init__(self, party):
        self.party = party

    def change_chair(self, number_chair):
        chair_count = self.party.elements.count(Chair())
        chair_max = Chair().max
        chair_min = Chair().min

        if number_chair < chair_min:
            number_chair = chair_min

        if number_chair > chair_max:
            number_chair = chair_max

        if number_chair > chair_count:
            self.add_chair(number_chair, chair_count)

        if number_chair < chair_count:
            self.remove_chair(number_chair)

    def remove_chair(self, number_chair):
        BuilderUtils(self.party).remove_element(number_chair, Chair)

    def add_chair(self, number_chair, chair_count):
        BuilderUtils(self.party).add_element(number_chair, chair_count, Chair)
