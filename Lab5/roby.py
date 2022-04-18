n = int(input())
if n == 0:
    print('0 0 0')
    exit()


def determinant3x3(array):
    plus = array[0][0] * array[1][1] * array[2][2] + array[2][0] * array[0][1] * array[1][2] + array[0][2] * array[1][
        0] * array[2][1]
    minus = array[0][2] * array[1][1] * array[2][0] + array[0][1] * array[1][0] * array[2][2] + array[2][1] * array[0][
        0] * array[1][2]
    return plus - minus


stanga, dreapta, drept = 0, 0, 0

primul = [int(x) for x in input().split()]
actual = primul[:]
pre = primul[:]

for i in range(n - 1):
    urmatorul = [int(x) for x in input().split()]
    if i > 0:
        arr = [[1, 1, 1], [pre[0], actual[0], urmatorul[0]], [pre[1], actual[1], urmatorul[1]]]
        det = determinant3x3(arr)

        if det == 0:
            drept += 1
        elif det < 0:
            dreapta += 1
        else:
            stanga += 1

    pre = actual
    actual = urmatorul

arr = [[1, 1, 1], [pre[0], actual[0], primul[0]], [pre[1], actual[1], primul[1]]]
det = determinant3x3(arr)

if det == 0:
    drept += 1
elif det < 0:
    dreapta += 1
else:
    stanga += 1

print(stanga, dreapta, drept)