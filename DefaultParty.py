from structure.Chaise import Chaise
from structure.Distributeur import Distributeur
from structure.Enceinte import Enceinte
from structure.Fontaine import Fontaine
from structure.Party import Party
from structure.Rampe import Rampe
from structure.Scene import Scene
from structure.Stand import Stand
from structure.Tente import Tente
from structure.Toilette import Toilette
from structure.Vigile import Vigile


def createDefaultParty():
    party = Party()

    party.Scene = Scene()
    party.rampe = Rampe()

    party.listVigile = [Vigile(), Vigile(), Vigile()]
    party.listChaise = [Chaise(), Chaise(), Chaise(), Chaise(), Chaise()]
    party.listDistributeur = [Distributeur()]
    party.listEnceinte = [Enceinte(), Enceinte()]
    party.listTente = [Tente(), Tente()]
    party.listToilette = [Toilette(), Toilette()]
    party.listFontaine = [Fontaine()]
    party.listStand = [Stand(), Stand(), Stand()]

    return party