def determinant3x3(array):
    plus = array[0][0] * array[1][1] * array[2][2] + array[2][0] * array[0][1] * array[1][2] + array[0][2] * array[1][
        0] * array[2][1]
    minus = array[0][2] * array[1][1] * array[2][0] + array[0][1] * array[1][0] * array[2][2] + array[2][1] * array[0][
        0] * array[1][2]
    return plus - minus


def laDreapta(point, line1, line2):
    arr = [[1, 1, 1], [line1[0], line2[0], point[0]], [line1[1], line2[1], point[1]]]
    det = determinant3x3(arr)
    return det < 0


n = int(input())

points = [input().split() for _ in range(n)]
points = [[int(x) for x in y] for y in points]


def Jarvis(n, points):
    A1 = min(points, key=lambda x: (x[0], x[1]))

    k = 1
    L = [A1]
    valid = True

    while valid:
        import random

        S = points[random.randint(0, len(points) - 1)]
        while S == L[-1]:
            S = points[random.randint(0, len(points) - 1)]

        for i in range(0, n):
            if laDreapta(points[i], L[-1], S):
                S = points[i]

        if S != A1:
            k += 1
            L.append(S)
        else:
            valid = False

    L.append(A1)

    return L


#print(Jarvis(n, points))
