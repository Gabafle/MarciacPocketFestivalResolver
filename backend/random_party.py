from backend.structure.Chaise import Chaise
from backend.structure.Distributeur import Distributeur
from backend.structure.Enceinte import Enceinte
from backend.structure.Fontaine import Fontaine
from backend.structure.Party import Party
from backend.structure.Rampe import Rampe
from backend.structure.Scene import Scene
from backend.structure.Stand import Stand
from backend.structure.Tente import Tente
from backend.structure.Toilette import Toilette
from backend.structure.Vigile import Vigile


class RandomParty:
    def generate(self):

        elements_constraints = {
            "bodyguard": (Vigile(), Vigile().min, Vigile().max),
            "chair": (Chaise(), Chaise().min, Chaise().max),
            "vending_machine": (Distributeur(), Distributeur().min, Distributeur().max),
            "speaker": (Enceinte(), Enceinte().min, Enceinte().max),
            "water_fountain": (Fontaine(), Fontaine().min, Fontaine().mac),
            "ramp": (Rampe(), Rampe().min, Rampe().max),
            "scene": (Scene(), Scene().min, Scene().max),
            "stand": (Stand(), Stand().min, Stand().max),
            "tent": (Tente(), Tente().min, Tente().max),
            "toilet": (Toilette(), Toilette().min, Toilette().max)
        }

        elements = []
        for name, (element, min_nb, _) in elements_constraints.items():
            elements.extend([element] * min_nb)
        return Party(elements)