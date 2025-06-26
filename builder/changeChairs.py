from DefaultParty import createDefaultParty
from structure.Chaise import Chaise


def changeChairs(numberschairs):
    newParty = createDefaultParty()

    if (type(numberschairs) != int):
        print("numberschairs is not an int")
    else:
        newParty.listChaise = createListChairs(numberschairs)

    return newParty


def createListChairs(numberschairs):
    if numberschairs < 4:
        numberschairs = 4
    if numberschairs > 6:
        numberschairs = 6

    listChairs = []

    for i in range(numberschairs):
        listChairs.append(Chaise())

    return listChairs
