from backend.buildeur.utils import BuilderUtils
from backend.structure.Water_fountain import Water_fountain


class changeWaterFontainService:
    def __init__(self, party):
        self.party = party

    def change_water_fontain(self, number_water_fontain):
        water_fontain_count = self.party.elements.count(Water_fountain())
        water_fontain_max = Water_fountain().max
        water_fontain_min = Water_fountain().min

        if number_water_fontain < water_fontain_min:
            number_water_fontain = water_fontain_min

        if number_water_fontain > water_fontain_max:
            number_water_fontain = water_fontain_max

        if number_water_fontain > water_fontain_count:
            self.add_water_fountain(number_water_fontain, water_fontain_count)

        if number_water_fontain < water_fontain_count:
            self.remove_water_fountain(number_water_fontain)

    def remove_water_fountain(self, number_water_fountain):
        BuilderUtils(self.party).remove_element(number_water_fountain, Water_fountain)

    def add_water_fountain(self, number_water_fountain, water_fountain_count):
        BuilderUtils(self.party).add_element(
            number_water_fountain, water_fountain_count, Water_fountain
        )
