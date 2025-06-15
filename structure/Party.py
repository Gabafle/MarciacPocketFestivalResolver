from structure.Rampe import Rampe
from structure.Scene import Scene


class Party:
    def __init__(self, scene=Scene(), rampe=Rampe(), listVigile=[], listChaise=[], listDistributeur=[], listEnceinte=[],
                 listFontaine=[], listStand=[], listToilette=[]):
        self.scene = scene
        self.rampe = rampe
        self.listVigile = listVigile
        self.listChaise = listChaise
        self.listDistributeur = listDistributeur
        self.listEnceinte = listEnceinte
        self.listFontaine = listFontaine
        self.listStand = listStand
        self.listToilette = listToilette

    def __repr__(self):  # ou __str__
        return f"Party({self.scene},{self.rampe},{self.listVigile},{self.listChaise},{self.listDistributeur},{self.listEnceinte},{self.listFontaine},{self.listStand},{self.listToilette})"

    def __eq__(self, other):
        if not isinstance(other, Party):
            return NotImplemented
        return (self.scene == other.scene and
                self.rampe == other.rampe and
                self.listVigile == other.listVigile and
                self.listChaise == other.listChaise and
                self.listDistributeur == other.listDistributeur and
                self.listEnceinte == other.listEnceinte and
                self.listFontaine == other.listFontaine and
                self.listStand == other.listStand and
                self.listToilette == other.listToilette)
