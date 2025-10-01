from backend.utils.utils_buildeur import UtilsBuildeur as ub


class BuilderUtils:
    def __init__(self, party):
        self.party = party

    def remove_element(self, number, type_element):
        """
        Supprime les éléments du type donné et en réajoute 'number' du même type.
        """
        # On filtre tout sauf les éléments du type donné
        party_elements_filtered = ub.remove_by_type(self.party.elements, [type_element])

        # On ajoute le nombre d'éléments spécifiés (instances)
        for i in range(number):
            party_elements_filtered.append(type_element())

        self.party.elements = party_elements_filtered

    def add_element(self, number, current_count, type_element):
        """
        Ajoute des éléments d'un type jusqu'à atteindre 'number'.
        """
        while current_count < number:
            self.party.elements.append(type_element())
            current_count += 1
