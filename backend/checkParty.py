from backend.structure.Party import Party


def verificationParty(party):
    if isinstance(party, Party):
        print("This element is not a party")
        return False
