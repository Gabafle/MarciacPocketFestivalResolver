from copy import deepcopy

from backend.DefaultParty import DefaultParty
from backend.structure.Party import Party
from backend.buildeur.Services import Services


class BuildeurParty(Party):

    def __init__(self, party=None):
        if party is None:
            self.party = DefaultParty().create()
        else:
            self.party = deepcopy(party)
        self.services = Services(self.party)

    def build(self):
        if len(self.party.elements) > 20:
            raise ValueError(
                f"Too many elements : The Party can t contain more than 20 elements. Actual Length : {len(self.party.elements)} Party Elements : {self.party.elements}"
            )

        return self.party

    def changeChair(self, number_chair):
        return self.services.chair_services.change_chair(number_chair)

    def changeBodyguard(self, number_bodyguard):
        return self.services.bodyguard_services.change_bodyguard(number_bodyguard)

    def changeSpeaker(self, number_speaker):
        return self.services.speaker_services.change_speaker(number_speaker)

    def changeStand(self, number_stand):
        return self.services.stand_services.change_stand(number_stand)

    def changeTent(self, number_tent):
        return self.services.tent_services.change_tent(number_tent)

    def changeToilet(self, number_toilet):
        return self.services.toilet_services.change_toilet(number_toilet)

    def changeVendingMachine(self, number_vending_machine):
        return self.services.vending_machine_services.change_vending_machine(
            number_vending_machine
        )

    def changeWaterFontain(self, number_water_fontain):
        return self.services.water_fontain_services.change_water_fontain(
            number_water_fontain
        )
