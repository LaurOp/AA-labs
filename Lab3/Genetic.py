import math
import random

# TODO COMMENT THE CODE

from Chromosome import Chromosome, recombine1breakPoint
import auxiliaries

populationSize, lowerBound, upperBound, coefficients, precision, \
crossoverProbability, mutationProbability, numberOfEpochs, chromosomeLength = auxiliaries.data.getAll()

file = open('evolutie.txt', 'w')
actualPopulation = []
maxChromosome = None

for epoch in range(numberOfEpochs):
    if epoch == 0:
        file.write('POPULATIE INITIALA : \n')

        for i in range(populationSize):
            aux = Chromosome(lowerBound, upperBound, chromosomeLength)
            if epoch == 0:
                file.write(
                    f'\t{i + 1}:\t{aux.bitlistToString()}\tx = {aux.bitlistToFloat()}\tf = {auxiliaries.functionToMaximize(aux.bitlistToFloat(), coefficients)}\n')
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
        poz = auxiliaries.binarySearch(u, probabilityIntervals)
        selection.append(actualPopulation[poz - 1])
        if epoch == 0:
            file.write(f'\tu = {u}\tselectam cromozomul {poz}\n')

    if epoch == 0:
        file.write('\nDupa selectie: \n')
        for i in range(populationSize):
            file.write(
                f'\t{i + 1}: {selection[i].bitlistToString()} x = {selection[i].bitlistToFloat()}\tf = {selection[i].functionValue}\n')

    toRecombine = []
    if epoch == 0:
        file.write(f'\nProbabilitatea de incrucisare {crossoverProbability}\n')
    for i in range(populationSize):
        u = random.uniform(0, 1)
        if epoch == 0:
            file.write(f'{i + 1}:\t{selection[i].bitlistToString()}\tu = {u}')
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
            file.write(f'Recombinam cromozomii {first[1] + 1} si {second[1] + 1} in punctul {pozBreak}:\n')
            file.write(f'\t\t\t{first[0].bitlistToString()}\t{second[0].bitlistToString()}\n')

        son, daughter = recombine1breakPoint(first[0], second[0], pozBreak)

        if epoch == 0:
            file.write(f'Results:\t{son.bitlistToString()}\t{daughter.bitlistToString()}\n\n')
        selection[first[1]] = son
        selection[second[1]] = daughter

    if epoch == 0:
        file.write('\nDupa recombinare: \n')
        for i in range(populationSize):
            file.write(
                f'\t{i + 1}: {selection[i].bitlistToString()} x = {selection[i].bitlistToFloat()}\tf = {selection[i].functionValue}\n')

        file.write('\nCromozomi supusi mutatiilor: \n')
    anyoneMutated = 0
    for i in range(populationSize):
        u = random.uniform(0, 1)
        if u < mutationProbability:
            if epoch == 0:
                file.write(f'{i + 1} ')
            anyoneMutated = 1
            selection[i].mutate()

    if epoch == 0:
        if anyoneMutated == 0:
            file.write('No mutations.\n')

    if epoch == 0:
        file.write('\n\nDupa mutatie: \n')
        for i in range(populationSize):
            file.write(
                f'\t{i + 1}: {selection[i].bitlistToString()} x = {selection[i].bitlistToFloat()}\tf = {selection[i].functionValue}\n')

    actualPopulation = selection.copy()

    if epoch != 0:
        minChromosome = min(selection, key=lambda x: x.functionValue)
        selection[selection.index(minChromosome)] = maxChromosome

    maxChromosome = max(selection, key=lambda x: x.functionValue)

    if epoch == 0:
        file.write('\nEvolutia maximului: \t\t\t Valoarea medie a performantei:\n\n')

    sumActual = 0
    for chromo in actualPopulation:
        sumActual += chromo.functionValue

    file.write(f'{str(maxChromosome.functionValue)}\t\t\t\t{sumActual / populationSize}')

file.close()
