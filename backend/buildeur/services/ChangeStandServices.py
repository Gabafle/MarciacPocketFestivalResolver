from backend.buildeur.utils import BuilderUtils
from backend.structure.Stand import Stand


class changeStandService:
    def __init__(self, party):
        self.party = party

    def change_stand(self, number_stand):
        stand_count = self.party.elements.count(Stand())
        stand_max = Stand().max
        stand_min = Stand().min

        if number_stand < stand_min:
            number_stand = stand_min

        if number_stand > stand_max:
            number_stand = stand_max

        if number_stand > stand_count:
            self.add_stand(number_stand, stand_count)

        if number_stand < stand_count:
            self.remove_stand(number_stand)

    def remove_stand(self, number_stand):
        BuilderUtils(self.party).remove_element(number_stand, Stand)

    def add_stand(self, number_stand, stand_count):
        BuilderUtils(self.party).add_element(number_stand, stand_count, Stand)
