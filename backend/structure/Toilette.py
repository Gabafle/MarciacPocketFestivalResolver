from backend.structure.Element import Element


class Toilette(Element):
    def __init__(self, score=100, width=2, height=2, max=2, min=1):
        super().__init__(score, width, height, max, min)

    def __repr__(self):  # ou __str__
        return f"Toilette(score='{self.score}', width={self.width}, height={self.height},max={self.max},min={self.min})"

    def __eq__(self, other):
        if not isinstance(other, Toilette):
            return NotImplemented
        return (self.score == other.score and
                self.width == other.width and
                self.height == other.height and
                self.max == other.max and
                self.min == other.min)