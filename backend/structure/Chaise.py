from backend.structure.Element import Element


class Chaise(Element):
    def __init__(self, score=50, width=1, height=1, max=6, min=4):
        super().__init__(score, width, height, max, min)

    def __repr__(self):  # ou __str__
        return f"Chaise(score='{self.score}', width={self.width}, height={self.height})"

    def __eq__(self, other):
        if not isinstance(other, Chaise):
            return NotImplemented
        return (
            self.score == other.score
            and self.width == other.width
            and self.height == other.height
        )
