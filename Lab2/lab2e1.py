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


print('\nCost nearest neighbour:', nearestNeighbour(orase, vecini, orase[0]))
print('Drum nearest neighbour:', solNearest)


# Algoritmul lui Prim; gaseste in O(m log n) un apcm

def PrimAlgorithm(cities, neighbours, start):
    Edges = []  # memoreaza muchiile APCM-ului
    Vertices = [start]  # urmareste varfurile adaugate in APCM
    Selected = defaultdict(lambda: 0)  # Dictionar de 'vizitati', pentru a verifica in O(1) daca varful este valabil
    Selected[start] = 1

    while len(Vertices) != len(cities):
        muchieMinima = None
        dimensiuneMinima = float('inf')
        for nod in Vertices:  # caut muchia (u,v) de cost minim, cu u in Edges si v in afara lui
            for vecin in neighbours[nod]:
                if Selected[vecin[0]] == 0:
                    if vecin[1] < dimensiuneMinima:
                        dimensiuneMinima = vecin[1]
                        muchieMinima = (nod, vecin[0], dimensiuneMinima)

        Edges.append(muchieMinima)
        Vertices.append(muchieMinima[1])
        Selected[muchieMinima[1]] = 1

    return Edges


rezultatDFS = []  # variabila globala care memoreaza turul eulerian


def DFS(graph, visited, actual=orase[0]):  # O(n) timp, O(n) memorie

    global rezultatDFS
    rezultatDFS.append(actual)
    visited[actual] = 1

    for vecin in graph[actual]:
        if visited[vecin[0]] == 0:
            DFS(graph, visited, vecin[0])

    rezultatDFS.append(actual)


# Double-tree , 2-aproximativ

def doubleTree(cities, neighbours, start=orase[0]):
    Edges = PrimAlgorithm(orase, vecini, orase[0])  # in Edges avem lista de muchii a APCM-ului

    Graf = defaultdict(lambda: [])  # Graf orientat obtinut din dublarea lui Edhges
    for edge in Edges:
        Graf[edge[0]].append((edge[1], edge[2]))
        Graf[edge[1]].append((edge[0], edge[2]))

    visitedDFS = defaultdict(lambda: 0)
    global rezultatDFS
    DFS(Graf, visitedDFS, start)  # obtinem in 'rezultatDFS' un tur eulerian

    rezultatDFS = list(dict.fromkeys(rezultatDFS))  # eliminam duplicatele din turul eulerian, obtinand 'scurtaturi'

    cost = 0  # calcul cost; este de maxim 2 ori mai rau decat optimul
    for i in range(-1, len(rezultatDFS) - 1):
        cost += dist(rezultatDFS[i], rezultatDFS[i + 1])
    print('\nCost double tree: ', cost)
    print('Drum double tree: ', rezultatDFS)


doubleTree(orase, vecini)
