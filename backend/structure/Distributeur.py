from backend.structure.Element import Element


class Distributeur(Element):
    def __init__(self, score=50, width=1, height=1,max=3,min=1):
       super().__init__(score,width,height,max,min)


    def __repr__(self):  # ou __str__
        return f"Distributeur(score='{self.score}', width={self.width}, height={self.height},max={self.max},min={self.min})"

    def __eq__(self, other):
        if not isinstance(other, Distributeur):
            return NotImplemented
        return (self.score == other.score and
                self.width == other.width and
                self.height == other.height and
                self.max == other.max and
                self.min == other.min)