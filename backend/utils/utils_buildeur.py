class UtilsBuildeur:

    @staticmethod
    def remove_by_type(elements, list_types_to_remove):
        elements_filtered = []
        for type_to_remove in list_types_to_remove:
            for element in elements:
                if not (isinstance(element, type_to_remove)):
                    elements_filtered.append(element)
        return elements_filtered
