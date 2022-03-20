import math
from collections import defaultdict


def citire(filepath):  # 1) citirea
    f = open(filepath)
    orase = f.readlines()
    orase = [x.strip().split(' ') for x in orase]
    orase = [(float(x[0]), float(x[1])) for x in orase]
    return orase


orase = citire('orase.txt')
print(orase)


def dist(oras1, oras2):  # 2) distanta
    return math.sqrt((oras2[0] - oras1[0]) ** 2 + (oras2[1] - oras1[1]) ** 2)


def completeGraph(cities):  # 3) graf complet de vecini, ponderat cu distantele
    neighb = defaultdict(lambda: [])

    for oras in cities:
        neighb[oras] = [(x, dist(oras, x)) for x in cities if x != oras]

    return neighb


vecini = completeGraph(orase)
# print(vecini)

lungmn = float('inf')
solmn = []
cond = 0

solActual = [orase[0]]
sumActual = 0
minSum = float('inf')
solFinal = []


def generatePathBrute(cities, neighbours, start):  # solutie brute force, O(n!)
    global solActual
    global minSum
    global solFinal
    global sumActual

    if len(solActual) == len(cities):
        sumActual += dist(start, solActual[0])
        if sumActual < minSum:
            minSum = sumActual
            solFinal = solActual.copy()
            if len(solActual) > 1:
                solFinal.append(solActual[0])
        sumActual -= dist(start, solActual[0])
    else:
        for vecin in neighbours[start]:
            if vecin[0] not in solActual:
                sumActual += vecin[1]
                solActual.append(vecin[0])
                generatePathBrute(cities, neighbours, vecin[0])
                sumActual -= vecin[1]
                solActual.pop()


generatePathBrute(orase, vecini, orase[0])
print('Cost minim:', minSum, '\nDrum minim: ', solFinal)

solNearest = []


def nearestNeighbour(cities, neighbours, start):
    global solNearest
    solNearest.append(start)
    cost = 0
    vecMinim = (0, 0)
    while len(solNearest) < len(cities):
        sMin = float('inf')
        for vecin in neighbours[start]:
            if vecin[0] not in solNearest:
                if vecin[1] < sMin:
                    vecMinim = vecin[0]
                    sMin = vecin[1]
        solNearest.append(vecMinim)
        cost += sMin

    if len(solNearest) > 1:
        solNearest.append(solNearest[0])
    cost += dist(vecMinim, solNearest[0])
    return cost


print('Cost nearest neighbour:', nearestNeighbour(orase, vecini, orase[0]))
print('Drum nearest neighbour:', solNearest)


