from backend.structure.Party import Party
from backend.structure.Rampe import Rampe
from backend.structure.Scene import Scene


def test_CreateEmptyParty():
    # Arrange
    listVigile = []
    listChaise = []
    listDistributeur = []
    listEnceinte = []
    listFontaine = []
    listStand = []
    listToilette = []

    partyExpected = f"Party({Scene()},{Rampe()},{listVigile},{listChaise},{listDistributeur},{listEnceinte},{listFontaine},{listStand},{listToilette})"

    # Act
    partyActual = Party()

    # Assert
    assert f"{partyActual}" == partyExpected
