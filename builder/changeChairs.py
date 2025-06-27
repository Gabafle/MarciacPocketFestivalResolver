from DefaultParty import createDefaultParty
from checkParty import verificationParty
from structure.Chaise import Chaise

def changeChairs(numberschairs, party):
    if verificationParty(party) == False:
        return createDefaultParty()
    if (type(numberschairs) != int):
        print("numberschairs is not an int")
    else:
        party.listChaise = createListChairs(numberschairs)

    return party


def createListChairs(numberschairs):
    if numberschairs < 4:
        numberschairs = 4
    if numberschairs > 6:
        numberschairs = 6

    listChairs = []

    for i in range(numberschairs):
        listChairs.append(Chaise())

    return listChairs
