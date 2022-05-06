xA, yA = input().split()
xB, yB = input().split()
xC, yC = input().split()
xD, yD = input().split()

xA, yA = int(xA), int(yA)
xB, yB = int(xB), int(yB)
xC, yC = int(xC), int(yC)
xD, yD = int(xD), int(yD)


def determinant3x3(array):
    plus = array[0][0] * array[1][1] * array[2][2] + array[2][0] * array[0][1] * array[1][2] + array[0][2] * array[1][
        0] * array[2][1]
    minus = array[0][2] * array[1][1] * array[2][0] + array[0][1] * array[1][0] * array[2][2] + array[2][1] * array[0][
        0] * array[1][2]
    return plus - minus


mat = [[xA - xD, yA - yD, xA * xA + yA * yA - xD * xD - yD * yD],
       [xB - xD, yB - yD, xB * xB + yB * yB - xD * xD - yD * yD],
       [xC - xD, yC - yD, xC * xC + yC * yC - xD * xD - yD * yD]]

det = determinant3x3(mat)

if det <= 0:
    print("AC: LEGAL")
elif det > 0:
    print("AC: ILLEGAL")

mat2 = [[xB - xA, yB - yA, xB * xB + yB * yB - xA * xA - yA * yA],
        [xC - xA, yC - yA, xC * xC + yC * yC - xA * xA - yA * yA],
        [xD - xA, yD - yA, xD * xD + yD * yD - xA * xA - yA * yA]]

det2 = determinant3x3(mat2)

if det2 <= 0:
    print("BD: LEGAL")
elif det2 > 0:
    print("BD: ILLEGAL")
