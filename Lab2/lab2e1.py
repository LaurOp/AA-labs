import math
from collections import defaultdict

f = open('orase.txt')
orase = f.readlines()
orase = [x.strip().split(' ') for x in orase]
orase = [(float(x[0]), float(x[1])) for x in orase]

print(orase)


def dist(oras1, oras2):
    return math.sqrt((oras2[0] - oras1[0]) ** 2 + (oras2[1] - oras1[1]) ** 2)


vecini = defaultdict(lambda: [])

for oras in orase:
    vecini[oras] = [(x, dist(oras, x)) for x in orase if x != oras]

lungmn = float('inf')
solmn = []
cond = 0


def generatePath(cities, vec, sol=[orase[0]], start=orase[0]):
    global lungmn
    global solmn
    print(sol)
    if len(sol) == len(cities):

        lung = 0
        for el in sol:
            lung += el[1]
        global lungmn
        if lung < lungmn:
            global solmn
            solmn = sol.copy()
            lungmn = lung

    else:
        for urmatoru in vec[start]:
            if urmatoru not in sol:

                generatePath(cities, vec, sol + [urmatoru], urmatoru)


generatePath(orase, vecini)
