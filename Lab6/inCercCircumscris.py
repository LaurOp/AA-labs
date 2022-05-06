def determinant3x3(array):
    plus = array[0][0] * array[1][1] * array[2][2] + array[2][0] * array[0][1] * array[1][2] + array[0][2] * array[1][
        0] * array[2][1]
    minus = array[0][2] * array[1][1] * array[2][0] + array[0][1] * array[1][0] * array[2][2] + array[2][1] * array[0][
        0] * array[1][2]
    return plus - minus


xA, yA = input().split()
xB, yB = input().split()
xC, yC = input().split()

xA, yA = int(xA), int(yA)
xB, yB = int(xB), int(yB)
xC, yC = int(xC), int(yC)

nrPuncte = int(input())

for _ in range(nrPuncte):
    xD, yD = input().split()
    xD, yD = int(xD), int(yD)

    mat = [[xA-xD, yA-yD, xA*xA + yA*yA - xD*xD - yD*yD],
           [xB-xD, yB-yD, xB*xB + yB*yB - xD*xD - yD*yD],
           [xC-xD, yC-yD, xC*xC + yC*yC - xD*xD - yD*yD]]

    det = determinant3x3(mat)

    if det == 0:
        print("BOUNDARY")
    elif det > 0:
        print("INSIDE")
    else:
        print("OUTSIDE")