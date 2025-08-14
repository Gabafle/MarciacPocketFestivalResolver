import random

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


class RandomParty:
    def generate(self, max_elements=20):

        elements_constraints = {
            "bodyguard": (Bodyguard(), Bodyguard().min, Bodyguard().max),
            "chair": (Chair(), Chair().min, Chair().max),
            "vending_machine": (
                Vending_machine(),
                Vending_machine().min,
                Vending_machine().max,
            ),
            "speaker": (Speaker(), Speaker().min, Speaker().max),
            "water_fountain": (
                Water_fountain(),
                Water_fountain().min,
                Water_fountain().max,
            ),
            "ramp": (Ramp(), Ramp().min, Ramp().max),
            "scene": (Scene(), Scene().min, Scene().max),
            "stand": (Stand(), Stand().min, Stand().max),
            "tent": (Tent(), Tent().min, Tent().max),
            "toilet": (Toilet(), Toilet().min, Toilet().max),
        }

        elements = []
        for _, (element, min_nb, _) in elements_constraints.items():
            elements.extend([element] * min_nb)

        remaining = max_elements - len(elements)

        possible_elements = []
        for _, (element, min_nb, max_nb) in elements_constraints.items():
            available_slots = max_nb - min_nb
            if available_slots > 0:
                possible_elements.extend([element] * available_slots)

        elements.extend(random.sample(possible_elements, remaining))

        return Party(elements)
