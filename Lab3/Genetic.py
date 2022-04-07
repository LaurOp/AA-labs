import math
import random

from Chromosome import Chromosome, recombine1breakPoint
import auxiliaries

populationSize, lowerBound, upperBound, coefficients, precision, \
crossoverProbability, mutationProbability, numberOfEpochs, chromosomeLength = auxiliaries.data.getAll()

file = open('evolutie.txt', 'w')
actualPopulation = []  # aici memoram populatia actuala; se pastreaza de la un pas la altul
maxChromosome = None

for epoch in range(numberOfEpochs):
    if epoch == 0:  # in prima generatie generam o populatie random
        file.write('POPULATIE INITIALA : \n')

        for i in range(populationSize):
            aux = Chromosome(lowerBound, upperBound, chromosomeLength)
            if epoch == 0:
                file.write(
                    f'\t{i + 1}:\t{aux.bitlistToString()}\tx = {aux.bitlistToFloat()}\tf = {auxiliaries.functionToMaximize(aux.bitlistToFloat(), coefficients)}\n')
            actualPopulation.append(aux)

    probabilityIntervals = [0]  # intervale de probabilitate, ajuta in procesul de selectie
    if epoch == 0:
        file.write('\n\nProbabilitati de selectie: \n')

    totalSumOfFunc = sum(
        [x.functionValue for x in actualPopulation])  # suma tuturor functionValues din populatia actuala
    for i in range(populationSize):
        probab = actualPopulation[
                     i].functionValue / totalSumOfFunc  # calculeaza probabilitatea cromozomului i de a fi selectat
        probabilityIntervals.append(probabilityIntervals[-1] + probab)
        if epoch == 0:
            file.write(f'\tChromosome {i + 1}\tprobability to be picked:\t{probab}\n')

    if math.floor(probabilityIntervals[-1]) != 1:  # un if ce se asigura ca ultimul element din intervale este 1
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

    selection = []  # un auxiliar ce va tine loc de populatie actuala pana la finalul generatiei
    file.write('\n\n')
    for i in range(populationSize):  # genereaza o noua populatie in functie de selectii (ponderate)
        u = random.uniform(0, 1)  # generez uniform un nr in [0,1)
        poz = auxiliaries.binarySearch(u, probabilityIntervals)
        selection.append(actualPopulation[poz - 1])
        if epoch == 0:
            file.write(f'\tu = {u}\tselectam cromozomul {poz}\n')

    if epoch == 0:
        file.write('\nDupa selectie: \n')
        for i in range(populationSize):
            file.write(
                f'\t{i + 1}: {selection[i].bitlistToString()} x = {selection[i].bitlistToFloat()}\tf = {selection[i].functionValue}\n')

    toRecombine = []  # memoram cromozomii ce intra in proces de recombinare
    if epoch == 0:
        file.write(f'\nProbabilitatea de incrucisare {crossoverProbability}\n')
    for i in range(populationSize):
        u = random.uniform(0, 1)
        if epoch == 0:
            file.write(f'{i + 1}:\t{selection[i].bitlistToString()}\tu = {u}')
        if u < crossoverProbability:  # atunci este ales pentru recombinare
            toRecombine.append((selection[i], i))
            if epoch == 0:
                file.write(' PARTICIPA ')
        if epoch == 0:
            file.write('\n')

    if epoch == 0:
        file.write('\n\n')
    while len(toRecombine) > 1:  # mergem pana la 1 exclusiv pentru a nu combina 1 cromozom cu sine
        first = toRecombine.pop()
        second = toRecombine.pop()
        pozBreak = random.randint(0, chromosomeLength)  # pozitia random la care se rup cromozomii in recombinare

        if epoch == 0:
            file.write(f'Recombinam cromozomii {first[1] + 1} si {second[1] + 1} in punctul {pozBreak}:\n')
            file.write(f'\t\t\t{first[0].bitlistToString()}\t{second[0].bitlistToString()}\n')

        son, daughter = recombine1breakPoint(first[0], second[0], pozBreak)  # recombinarea

        if epoch == 0:
            file.write(f'Results:\t{son.bitlistToString()}\t{daughter.bitlistToString()}\n\n')

        # inlocuirea in populatie
        selection[first[1]] = son
        selection[second[1]] = daughter

    if epoch == 0:
        file.write('\nDupa recombinare: \n')
        for i in range(populationSize):
            file.write(
                f'\t{i + 1}: {selection[i].bitlistToString()} x = {selection[i].bitlistToFloat()}\tf = {selection[i].functionValue}\n')

        file.write('\nCromozomi supusi mutatiilor: \n')
    anyoneMutated = 0  # auxiliara pentru afisare
    for i in range(populationSize):  # decidem ce cromozomi sunt supusi mutatiilor
        u = random.uniform(0, 1)
        if u < mutationProbability:
            if epoch == 0:
                file.write(f'{i + 1} ')
            anyoneMutated = 1
            selection[i].mutate()  # metoda clasei Chromosome; schimba un bit in opusul sau

    if epoch == 0:
        if anyoneMutated == 0:
            file.write('No mutations.\n')

    if epoch == 0:
        file.write('\n\nDupa mutatie: \n')
        for i in range(populationSize):
            file.write(
                f'\t{i + 1}: {selection[i].bitlistToString()} x = {selection[i].bitlistToFloat()}\tf = {selection[i].functionValue}\n')

    actualPopulation = selection.copy()  # mutam auxiliarul de pana acum in populatia efectiva, pentru a o pasa mai departe

    if epoch != 0:  # selectia elitista;    se intampla de la generatia 2 incolo
        minChromosome = min(selection, key=lambda x: x.functionValue)  # cromozomul minim isi pierde locul in populatie
        selection[selection.index(minChromosome)] = maxChromosome  # in favoarea celui mai bun cromozom

    maxChromosome = max(selection, key=lambda x: x.functionValue)  # tinem minte cromozomul maxim pentru a-l pastra
                                                                   # intre generatii

    if epoch == 0:
        file.write('\nEvolutia maximului: \t\t\t Valoarea medie a performantei:\n\n')

    sumActual = 0   # Valoarea medie a functiei in cadrul populatiei actuale (per generatie)
    for chromo in actualPopulation:
        sumActual += chromo.functionValue

    file.write(f'{str(maxChromosome.functionValue)}\t\t\t\t{sumActual / populationSize}')

file.close()
