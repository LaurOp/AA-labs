import math


# polinomiala de orice grad
def functionToMaximize(x, coeffs):
    s = 0
    p = 0

    for coef in reversed(coeffs):
        s += (x ** p) * coef
        p += 1

    return s


def inputForAlgorithm():
    populationSize = int(input('Dimensiunea populatiei: ').strip())  # 20

    lowerBound = int(input('Limita inferioara a domeniului: ').strip())  # -1
    upperBound = int(input('Limita superioara a domeniului: ').strip())  # 2
    while upperBound < lowerBound:
        print('Lower bound was bigger than Upper bound!')
        lowerBound = int(input('Limita inferioara a domeniului: ').strip())
        upperBound = int(input('Limita superioara a domeniului: ').strip())

    coefficients = []  # -1, 1, 2

    nr = int(input('Gradul polinomului: ').strip())     # 2
    print("De la grad mare la mic!")
    for i in range(nr + 1):
        aux = int(input(f'Coeficientul {i + 1}: ').strip())
        coefficients.append(aux)

    precision = int(input('Precision: ').strip())  # 6

    crossoverProbability = float(input('Probabilitatea de recombinare (1-100) : ').strip()) / 100  # 0.25

    mutationProbability = float(input('Probabilitatea de mutatie (1-100) : ').strip()) / 100  # 0.01

    numberOfEpochs = int(input('Numar de etape ale algoritmului: ').strip())  # 50

    chromosomeLength = math.ceil(math.log2((10 ** precision) * (upperBound - lowerBound)))

    if lowerBound == upperBound:
        print(functionToMaximize(lowerBound, coefficients))
        exit()

    return populationSize, lowerBound, upperBound, coefficients, precision, crossoverProbability, mutationProbability, numberOfEpochs, chromosomeLength


class InputData:
    def __init__(self):
        self.populationSize, self.lowerBound, self.upperBound, self.coefficients, self.precision, \
        self.crossoverProbability, self.mutationProbability, self.numberOfEpochs, self.chromosomeLength = inputForAlgorithm()

    def getAll(self):
        return self.populationSize, self.lowerBound, self.upperBound, self.coefficients, self.precision, self.crossoverProbability, self.mutationProbability, self.numberOfEpochs, self.chromosomeLength

data = InputData()


def binarySearch(value, array):
    left = 0
    right = len(array)

    while left <= right:
        mid = (left + right) // 2
        if value == array[mid]:
            return mid + 1
        if value < array[mid]:
            right = mid
        else:
            if value < array[mid + 1]:
                return mid + 1
            left = mid

    return None



