from backend.structure.Party import Party

def verificationParty(party):
    if (type(party) != Party):
        print("This element is not a party")
        return False