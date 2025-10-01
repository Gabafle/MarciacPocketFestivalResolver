from backend.buildeur.utils import BuilderUtils
from backend.structure.Toilet import Toilet


class changeToiletService:
    def __init__(self, party):
        self.party = party

    def change_toilet(self, number_toilet):
        toilet_count = self.party.elements.count(Toilet())
        toilet_max = Toilet().max
        toilet_min = Toilet().min

        if number_toilet < toilet_min:
            number_toilet = toilet_min

        if number_toilet > toilet_max:
            number_toilet = toilet_max

        if number_toilet > toilet_count:
            self.add_toilet(number_toilet, toilet_count)

        if number_toilet < toilet_count:
            self.remove_toilet(number_toilet)

    def remove_toilet(self, number_toilet):
        BuilderUtils(self.party).remove_element(number_toilet, Toilet)

    def add_toilet(self, number_toilet, toilet_count):
        BuilderUtils(self.party).add_element(number_toilet, toilet_count, Toilet)
