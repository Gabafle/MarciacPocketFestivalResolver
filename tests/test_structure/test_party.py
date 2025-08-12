from backend.structure.Party import Party
from backend.structure.Rampe import Rampe
from backend.structure.Scene import Scene


def test_CreateEmptyParty():
    # Arrange
    partyExpected =[]

    # Act
    partyActual = Party()

    # Assert
    assert partyActual.elements == partyExpected
