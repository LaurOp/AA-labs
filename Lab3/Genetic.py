import math
import random

populationSize = 20  # int(input('Dimensiunea populatiei: ').strip())

lowerBound = -1  # int(input('Limita inferioara a domeniului: ').strip())
upperBound = 2  # int(input('Limita superioara a domeniului: ').strip())
# while upperBound < lowerBound:
#     lowerBound = int(input('Limita inferioara a domeniului: ').strip())
#     upperBound = int(input('Limita superioara a domeniului: ').strip())

coefficients = [-1, 1, 2]
# nr = #int(input('Gradul polinomului: ').strip())
# for i in range(nr + 1):
#     aux = int(input(f'Coeficientul {i + 1} :').strip())
#     coefficients.append(aux)

precision = 6  # int(input('Precision: ').strip())

crossoverProbability = 0.25  # float(input('Probabilitatea de recombinare: ').strip()) / 100

mutationProbability = 0.01  # float(input('Probabilitatea de mutatie: ').strip()) / 100

numberOfEpochs = 50  # int(input('Numar de etape ale algoritmului: ').strip())

chromosomeLength = math.ceil(math.log2((10 ** precision) * (upperBound - lowerBound)))


# polinomiala de orice grad
def functionToMaximize(x, coefficients):
    s = 0
    p = 0

    for coef in reversed(coefficients):
        s += (x ** p) * coef
        p += 1

    return s


if lowerBound == upperBound:
    print(functionToMaximize(lowerBound, coefficients))
    exit()


def binarySearch(value, array):
    left = 0
    right = len(array)

    while left <= right:
        mid = (left + right) // 2
        if value == array[mid]:
            return mid+1
        if value < array[mid]:
            right = mid
        else:
            if value < array[mid+1]:
                return mid+1
            left = mid

    return None


def recombine1breakPoint(first, second, position):  # first and second are Chromosomes
    if position == 0:
        return first, second

    a = Chromosome(first.lowerbound, first.upperbound, chromosomeLength, second.bitsList[:position] + first.bitsList[position:])
    b = Chromosome(first.lowerbound, first.upperbound, chromosomeLength, first.bitsList[:position] + second.bitsList[position:])

    return a, b


class Chromosome:
    nrOfBits = 0    # static

    def __init__(self, lowerbound, upperbound, noOfBits=0, bitlist=[]):
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
        self.bitsList[pozMutatie-1] = True if self.bitsList[pozMutatie-1] is False else False
        self.functionValue = functionToMaximize(self.bitlistToFloat(), coefficients)


Chromosome.nrOfBits = chromosomeLength


file = open('evolutie.txt', 'w')
actualPopulation = []
maxChromosome = None

for epoch in range(numberOfEpochs):
    if epoch == 0:
        file.write('POPULATIE INITIALA : \n')

        for i in range(populationSize):
            aux = Chromosome(lowerBound, upperBound, chromosomeLength)
            if epoch == 0:
                file.write(f'\t{i + 1}:\t{aux.bitlistToString()}\tx = {aux.bitlistToFloat()}\tf = {functionToMaximize(aux.bitlistToFloat(), coefficients)}\n')
            actualPopulation.append(aux)


    probabilityIntervals = [0]
    if epoch == 0:
        file.write('\n\nProbabilitati de selectie: \n')

    totalSumOfFunc = sum([x.functionValue for x in actualPopulation])
    for i in range(populationSize):
        probab = actualPopulation[i].functionValue / totalSumOfFunc
        probabilityIntervals.append(probabilityIntervals[-1] + probab)
        if epoch == 0:
            file.write(f'\tChromosome {i + 1}\tprobability to be picked:\t{probab}\n')

    if math.floor(probabilityIntervals[-1]) != 1:
        probabilityIntervals.append(1)
    else:
        probabilityIntervals[-1] = 1.0

    if epoch == 0:
        file.write('\n Intervale de probabilitati de selectie: \n\t\t')
        nr = 0
        for el in probabilityIntervals:
            nr += 1
            file.write(f'\t{el}\t')
            if nr % 3 == 0:
                file.write('\n')


    selection = []
    file.write('\n\n')
    for i in range(populationSize):
        u = random.uniform(0, 1)
        poz = binarySearch(u, probabilityIntervals)
        selection.append(actualPopulation[poz-1])
        if epoch == 0:
            file.write(f'\tu = {u}\tselectam cromozomul {poz}\n')


    if epoch == 0:
        file.write('\nDupa selectie: \n')
        for i in range(populationSize):
            file.write(f'\t{i+1}: {selection[i].bitlistToString()} x = {selection[i].bitlistToFloat()}\tf = {selection[i].functionValue}\n')



    toRecombine = []
    if epoch == 0:
        file.write(f'\nProbabilitatea de incrucisare {crossoverProbability}\n')
    for i in range(populationSize):
        u = random.uniform(0, 1)
        if epoch == 0:
            file.write(f'{i+1}:\t{selection[i].bitlistToString()}\tu = {u}')
        if u < crossoverProbability:
            toRecombine.append((selection[i], i))
            if epoch == 0:
                file.write(' PARTICIPA ')
        if epoch == 0:
            file.write('\n')


    if epoch == 0:
        file.write('\n\n')
    while len(toRecombine) > 1:
        first = toRecombine.pop()
        second = toRecombine.pop()
        pozBreak = random.randint(0, chromosomeLength)

        if epoch == 0:
            file.write(f'Recombinam cromozomii {first[1]+1} si {second[1]+1} in punctul {pozBreak}:\n')
            file.write(f'\t\t\t{first[0].bitlistToString()}\t{second[0].bitlistToString()}\n')

        son, daughter = recombine1breakPoint(first[0], second[0], pozBreak)

        if epoch == 0:
            file.write(f'Results:\t{son.bitlistToString()}\t{daughter.bitlistToString()}\n\n')
        selection[first[1]] = son
        selection[second[1]] = daughter

    if epoch == 0:
        file.write('\nDupa recombinare: \n')
        for i in range(populationSize):
            file.write(f'\t{i+1}: {selection[i].bitlistToString()} x = {selection[i].bitlistToFloat()}\tf = {selection[i].functionValue}\n')


        file.write('\nCromozomi supusi mutatiilor: \n')
    anyoneMutated = 0
    for i in range(populationSize):
        u = random.uniform(0, 1)
        if u < mutationProbability:
            if epoch == 0:
                file.write(f'{i+1} ')
            anyoneMutated = 1
            selection[i].mutate()

    if epoch == 0:
        if anyoneMutated == 0:
            file.write('No mutations.\n')


    if epoch == 0:
        file.write('\n\nDupa mutatie: \n')
        for i in range(populationSize):
            file.write(f'\t{i + 1}: {selection[i].bitlistToString()} x = {selection[i].bitlistToFloat()}\tf = {selection[i].functionValue}\n')


    actualPopulation = selection.copy()

    if epoch != 0:
        minChromosome = min(selection, key=lambda x: x.functionValue)
        selection[selection.index(minChromosome)] = maxChromosome

    maxChromosome = max(selection, key=lambda x: x.functionValue)

    if epoch == 0:
        file.write('\nEvolutia maximului: \n\n')

    file.write(str(maxChromosome.functionValue))


file.close()