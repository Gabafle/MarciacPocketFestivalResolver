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


def createDefaultParty():
    party = Party()

    party.Scene = Scene()
    party.rampe = Rampe()

    party.listVigile = [Vigile(), Vigile(), Vigile()]
    party.listChaise = [Chaise(), Chaise(), Chaise(), Chaise()]
    party.listDistributeur = [Distributeur()]
    party.listEnceinte = [Enceinte(), Enceinte()]
    party.listTente = [Tente(), Tente()]
    party.listToilette = [Toilette(), Toilette()]
    party.listFontaine = [Fontaine()]
    party.listStand = [Stand(), Stand(), Stand()]

    return party