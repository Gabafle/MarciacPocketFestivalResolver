from backend.structure.Chair import Chair
from backend.structure.Vending_machine import Vending_machine
from backend.structure.Speaker import Speaker
from backend.structure.Water_fountain import Water_fountain
from backend.structure.Party import Party
from backend.structure.Ramp import Ramp
from backend.structure.Scene import Scene
from backend.structure.Stand import Stand
from backend.structure.Tent import Tent
from backend.structure.Toilet import Toilet
from backend.structure.Bodyguard import Bodyguard


class DefaultParty:

    @staticmethod
    def create():
        party = Party()

        party.elements = [
            Bodyguard(),
            Bodyguard(),
            Bodyguard(),
            Chair(),
            Chair(),
            Chair(),
            Chair(),
            Scene(),
            Ramp(),
            Vending_machine(),
            Speaker(),
            Speaker(),
            Tent(),
            Tent(),
            Toilet(),
            Toilet(),
            Water_fountain(),
            Stand(),
            Stand(),
            Stand(),
        ]
        return party
