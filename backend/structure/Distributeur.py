class Distributeur:
    def __init__(self, score=50, width=1, height=1):
        self.score = score
        self.width = width
        self.height = height


    def __repr__(self):  # ou __str__
        return f"Distributeur(score='{self.score}', width={self.width}, height={self.height})"

    def __eq__(self, other):
        if not isinstance(other, Distributeur):
            return NotImplemented
        return (self.score == other.score and
                self.width == other.width and
                self.height == other.height)