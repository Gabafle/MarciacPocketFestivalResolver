from backend.structure.Party import Party


def test_CreateEmptyParty():
    # Arrange
    party_expected = []

    # Act
    party_actual = Party()

    # Assert
    assert party_actual.elements == party_expected
