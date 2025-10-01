from backend.buildeur.utils import BuilderUtils
from backend.structure.Vending_machine import Vending_machine


class changeVendingMachineService:
    def __init__(self, party):
        self.party = party

    def change_vending_machine(self, number_vending_machine):
        vending_machine_count = self.party.elements.count(Vending_machine())
        vending_machine_max = Vending_machine().max
        vending_machine_min = Vending_machine().min

        if number_vending_machine < vending_machine_min:
            number_vending_machine = vending_machine_min

        if number_vending_machine > vending_machine_max:
            number_vending_machine = vending_machine_max

        if number_vending_machine > vending_machine_count:
            self.add_vending_machine(number_vending_machine, vending_machine_count)

        if number_vending_machine < vending_machine_count:
            self.remove_vending_machine(number_vending_machine)

    def remove_vending_machine(self, number_vending_machine):
        BuilderUtils(self.party).remove_element(number_vending_machine, Vending_machine)

    def add_vending_machine(self, number_vending_machine, vending_machine_count):
        BuilderUtils(self.party).add_element(
            number_vending_machine, vending_machine_count, Vending_machine
        )
