from backend.buildeur.utils import BuilderUtils
from backend.structure.Tent import Tent


class changeTentService:
    def __init__(self, party):
        self.party = party

    def change_tent(self, number_tent):
        tent_count = self.party.elements.count(Tent())
        tent_max = Tent().max
        tent_min = Tent().min

        if number_tent < tent_min:
            number_tent = tent_min

        if number_tent > tent_max:
            number_tent = tent_max

        if number_tent > tent_count:
            self.add_tent(number_tent, tent_count)

        if number_tent < tent_count:
            self.remove_tent(number_tent)

    def remove_tent(self, number_tent):
        BuilderUtils(self.party).remove_element(number_tent, Tent)

    def add_tent(self, number_tent, tent_count):
        BuilderUtils(self.party).add_element(number_tent, tent_count, Tent)
