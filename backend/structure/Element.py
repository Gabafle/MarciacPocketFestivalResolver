class Element:
    def __init__(self, score, width, height,max,min):
        self.score = score
        self.width = width
        self.height = height
        self.max = max
        self.min = min
    def __eq__(self, other):
        if not isinstance(other, Element):
            return NotImplemented
        return (self.score == other.score and
                self.width == other.width and
                self.height == other.height)