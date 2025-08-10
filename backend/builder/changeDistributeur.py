from backend.DefaultParty import createDefaultParty
from backend.checkParty import verificationParty
from backend.structure.Distributeur import Distributeur


def changeDistributeur(numberDistributeur,party):
    if verificationParty(party) == False:
        return createDefaultParty()

    newListDistributeur = []
    if numberDistributeur < 1:
        numberDistributeur = 1
    if numberDistributeur > 3:
        numberDistributeur = 3

    for i in range(numberDistributeur):
        newListDistributeur.append(Distributeur())

    party.listDistributeur = newListDistributeur

    return party
