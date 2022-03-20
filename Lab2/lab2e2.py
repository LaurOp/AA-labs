class Chromosome:
    def __init__(self, lowerbound, upperbound, nrOfBits):
        self.lowerbound = lowerbound
        self.upperbound = upperbound
        self.nrOfBits = nrOfBits
        self.bitsList = [False for _ in range(self.nrOfBits)]
        self.precision = (self.upperbound - self.lowerbound) / (2**self.nrOfBits)

    def bitlistToFloat(self):
        nr = 0
        p = 1
        for bit in reversed(self.bitsList): # a) bitlist -> float
            nr += int(bit)*p
            p *= 2

        nr *= self.precision    # b) inmultit cu incrementul

        return nr + self.lowerbound     # c) adun la capatul stang


cr = Chromosome(0, 100, 5)
print(cr.bitlistToFloat())
cr.bitsList = [False, False, True, True, False]
print(cr.bitlistToFloat())