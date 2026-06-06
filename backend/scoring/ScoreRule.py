class ScoreRule:
    """
    Règle de score basée sur la proximité entre deux types d'éléments.

    Attributs :
        source_type  : type de l'élément déclencheur (ex: Chair)
        target_type  : type de l'élément voisin recherché (ex: Speaker)
        bonus        : points ajoutés (positif) ou retirés (négatif)
        description  : texte affiché dans le panneau de score
        bidirectional: si True, la règle s'applique dans les deux sens
    """

    def __init__(
        self, source_type, target_type, bonus, description, bidirectional=True
    ):
        self.source_type = source_type
        self.target_type = target_type
        self.bonus = bonus
        self.description = description
        self.bidirectional = bidirectional
