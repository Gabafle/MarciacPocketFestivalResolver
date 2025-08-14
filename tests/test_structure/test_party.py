from backend.structure.Party import Party


def test_CreateEmptyParty():
    # Arrange
    partyExpected = []

    # Act
    partyActual = Party()

    # Assert
    assert partyActual.elements == partyExpected
