n = int(input())

puncte = []

for _ in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    puncte.append((x, y))

stanga, dreapta, jos, sus = puncte[0], puncte[0], puncte[0], puncte[0]
ist, idr, ijos, isus = 0, 0, 0, 0

for i, elem in enumerate(puncte):
    if elem[0] < stanga[0]:
        stanga = elem
        ist = i
    if elem[0] > dreapta[0]:
        dreapta = elem
        idr = i
    if elem[1] < jos[1]:
        jos = elem
        ijos = i
    if elem[1] > sus[1]:
        sus = elem
        isus = i

# print(stanga, dreapta, jos, sus)
# print(ist, idr, ijos, isus)

sirX1 = []
sirX2 = []

if ist < idr:
    for i in range(ist, idr+1):
        sirX1.append(puncte[i])

    for i in range(idr, n):
        sirX2.append(puncte[i])
    for i in range(0, ist + 1):
        sirX2.append(puncte[i])
else:
    for i in range(idr, ist + 1):
        sirX1.append(puncte[i])

    for i in range(ist, n):
        sirX2.append(puncte[i])
    for i in range(0, idr + 1):
        sirX2.append(puncte[i])


sirX2.reverse()

# print(sirX1)
# print(sirX2)

conditieX = True

for i in range(1, len(sirX1)):
    if sirX1[i][0] < sirX1[i-1][0]:
        conditieX = False
        break

if conditieX:
    for i in range(1, len(sirX2)):
        if sirX2[i][0] < sirX2[i-1][0]:
            conditieX = False
            break

if conditieX:
    print("YES")
else:
    print("NO")

sirY1 = []
sirY2 = []

if ijos < isus:
    for i in range(ijos, isus+1):
        sirY1.append(puncte[i])

    for i in range(isus, n):
        sirY2.append(puncte[i])
    for i in range(0, ijos + 1):
        sirY2.append(puncte[i])
else:
    for i in range(isus, ijos + 1):
        sirX1.append(puncte[i])

    for i in range(ijos, n):
        sirY2.append(puncte[i])
    for i in range(0, isus + 1):
        sirY2.append(puncte[i])

sirY2.reverse()

# print(sirY1)
# print(sirY2)

conditieY = True

for i in range(1, len(sirY1)):
    if sirY1[i][1] < sirY1[i-1][1]:
        conditieY = False
        break

if conditieY:
    for i in range(1, len(sirY2)):
        if sirY2[i][1] < sirY2[i-1][1]:
            conditieY = False
            break

if conditieY:
    print("YES")
else:
    print("NO")
