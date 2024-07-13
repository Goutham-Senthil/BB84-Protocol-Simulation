import random

class Qubit:
    def __init__(self, bloch):
        self.bloch = bloch

    def measure(self, rotation):
        if rotation == "horizontal":
            if self.bloch == 90 or self.bloch == 270:
                return int(self.bloch == 270)
            else:
                self.bloch = 90 if random.randint(0, 1) == 1 else 270
                return int(self.bloch == 90)

        elif rotation == "vertical":
            if self.bloch == 0 or self.bloch == 180:
                return int(self.bloch == 180)
            else:
                self.bloch = 0 if random.randint(0, 1) == 1 else 180
                return int(self.bloch == 0)
