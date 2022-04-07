import random

from auxiliaries import functionToMaximize, data

# coeficientii polinomului de maximizat
coefficients = data.coefficients


class Chromosome:
    nrOfBits = data.chromosomeLength  # static  , lungimea calculata a unui cromozom

    def __init__(self, lowerbound, upperbound, noOfBits=0, bitlist=None):
        if bitlist is None:
            bitlist = []
        self.lowerbound = lowerbound
        self.upperbound = upperbound
        self.bitsList = [random.choice([True, False]) for _ in range(self.nrOfBits)] if len(bitlist) == 0 else bitlist
        self.precision = (self.upperbound - self.lowerbound) / (2 ** self.nrOfBits - 1)
        self.functionValue = functionToMaximize(self.bitlistToFloat(), coefficients)    # calculez la initializare valoarea functiei

    def bitlistToFloat(self):   # trecere din lista de biti in Float
        nr = 0
        p = 1
        for bit in reversed(self.bitsList):  # a) bitlist -> float
            nr += int(bit) * p
            p *= 2

        nr *= self.precision  # b) inmultit cu incrementul

        return nr + self.lowerbound  # c) adun la capatul stang

    def bitlistToString(self):      # trecere din lista de biti in String
        s = ""
        for bit in self.bitsList:
            if bit is False:
                s += '0'
            else:
                s += '1'
        return s

    def mutate(self):       # mutatie pe un bit random
        pozMutatie = random.randint(0, self.nrOfBits)
        self.bitsList[pozMutatie - 1] = True if self.bitsList[pozMutatie - 1] is False else False
        self.functionValue = functionToMaximize(self.bitlistToFloat(), coefficients)    # update valorii functiei in cromozomul respectiv


def recombine1breakPoint(first, second, position):  # first and second are Chromosomes
    if position == 0:
        return first, second

    # recombin lista de biti a celor 2 cromozomi si ii intorc
    a = Chromosome(first.lowerbound, first.upperbound, data.chromosomeLength,
                   second.bitsList[:position] + first.bitsList[position:])
    b = Chromosome(first.lowerbound, first.upperbound, data.chromosomeLength,
                   first.bitsList[:position] + second.bitsList[position:])

    return a, b
