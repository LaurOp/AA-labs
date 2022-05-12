# functie de calculat un determinant 3x3 fara numpy (nu merge numpy pe site)
def determinant3x3(array):
    plus = array[0][0] * array[1][1] * array[2][2] + array[2][0] * array[0][1] * array[1][2] + array[0][2] * array[1][
        0] * array[2][1]
    minus = array[0][2] * array[1][1] * array[2][0] + array[0][1] * array[1][0] * array[2][2] + array[2][1] * array[0][
        0] * array[1][2]
    return plus - minus


# inputuri
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
    # calculul acelui determinant 4x4 , pe care l-am simplificat la 3x3 prin scaderea ultimei linii peste tot
    mat = [[xA - xD, yA - yD, xA * xA + yA * yA - xD * xD - yD * yD],
           [xB - xD, yB - yD, xB * xB + yB * yB - xD * xD - yD * yD],
           [xC - xD, yC - yD, xC * xC + yC * yC - xD * xD - yD * yD]]

    det = determinant3x3(mat)

    # pozitia fata de cerc
    if det == 0:
        print("BOUNDARY")
    elif det > 0:
        print("INSIDE")
    else:
        print("OUTSIDE")
