from backend.structure.Element import Element


class Chair(Element):
    def __init__(self, score=50, width=1, height=1, max=6, min=4):
        super().__init__(score, width, height, max, min)

    def __repr__(self):  # ou __str__
        return f"Chair(score='{self.score}', width={self.width}, height={self.height})"

    def __eq__(self, other):
        if not isinstance(other, Chair):
            return NotImplemented
        return (self.score == other.score and
                self.width == other.width and
                self.height == other.height)
