n = int(input())


def determinant3x3(array):
    plus = array[0][0] * array[1][1] * array[2][2] + array[2][0] * array[0][1] * array[1][2] + array[0][2] * array[1][
        0] * array[2][1]
    minus = array[0][2] * array[1][1] * array[2][0] + array[0][1] * array[1][0] * array[2][2] + array[2][1] * array[0][
        0] * array[1][2]
    return plus - minus


primul = [int(x) for x in input().split()]
if n == 1:
    print(1)
    print(primul[0], primul[1])
    exit()

start = primul[:]

actual = [int(x) for x in input().split()]
if n == 2:
    print(2)
    print(primul[0], primul[1])
    print(actual[0], actual[1])
    exit()

result = [actual]

for _ in range(n - 2):
    actual = [int(x) for x in input().split()]

    arr = [[1, 1, 1], [start[0], result[-1][0], actual[0]], [start[1], result[-1][1], actual[1]]]
    det = determinant3x3(arr)

    if det <= 0:  # dreapta
        result.pop()
        result.append(actual)
    else:  # stanga
        start = result[-1]
        result.append(actual)

arr = [[1, 1, 1], [start[0], result[-1][0], primul[0]], [start[1], result[-1][1], primul[1]]]
det = determinant3x3(arr)

if det <= 0:  # dreapta
    if result[-1] != start:
        result.pop()
    result.append(primul)
# else:
#     arr = [[1, 1, 1], [start[0], result[-1][0], result[0][0]], [start[1], result[-1][1], result[0][1]]]
#     det = determinant3x3(arr)

print(len(result))
for el in result:
    print(el[0], el[1])
