import random

from auxiliaries import functionToMaximize, data

coefficients = data.coefficients


class Chromosome:
    nrOfBits = data.chromosomeLength  # static

    def __init__(self, lowerbound, upperbound, noOfBits=0, bitlist=None):
        if bitlist is None:
            bitlist = []
        self.lowerbound = lowerbound
        self.upperbound = upperbound
        self.bitsList = [random.choice([True, False]) for _ in range(self.nrOfBits)] if len(bitlist) == 0 else bitlist
        self.precision = (self.upperbound - self.lowerbound) / (2 ** self.nrOfBits - 1)
        self.functionValue = functionToMaximize(self.bitlistToFloat(), coefficients)

    def bitlistToFloat(self):
        nr = 0
        p = 1
        for bit in reversed(self.bitsList):  # a) bitlist -> float
            nr += int(bit) * p
            p *= 2

        nr *= self.precision  # b) inmultit cu incrementul

        return nr + self.lowerbound  # c) adun la capatul stang

    def bitlistToString(self):
        s = ""
        for bit in self.bitsList:
            if bit is False:
                s += '0'
            else:
                s += '1'
        return s

    def mutate(self):
        pozMutatie = random.randint(0, self.nrOfBits)
        self.bitsList[pozMutatie - 1] = True if self.bitsList[pozMutatie - 1] is False else False
        self.functionValue = functionToMaximize(self.bitlistToFloat(), coefficients)


def recombine1breakPoint(first, second, position):  # first and second are Chromosomes
    if position == 0:
        return first, second

    a = Chromosome(first.lowerbound, first.upperbound, data.chromosomeLength,
                   second.bitsList[:position] + first.bitsList[position:])
    b = Chromosome(first.lowerbound, first.upperbound, data.chromosomeLength,
                   first.bitsList[:position] + second.bitsList[position:])

    return a, b
