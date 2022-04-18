t = int(input())

def determinant3x3(array):
    plus = array[0][0]*array[1][1]*array[2][2] + array[2][0]*array[0][1]*array[1][2] + array[0][2]*array[1][0]*array[2][1]
    minus = array[0][2]*array[1][1]*array[2][0] + array[0][1]*array[1][0]*array[2][2] + array[2][1]*array[0][0]*array[1][2]
    return plus-minus

for _ in range(t):
    inp = input().split()
    px, py, qx, qy, rx, ry = int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3]), int(inp[4]), int(inp[5])
    arr = [[1, 1, 1], [px, qx, rx], [py, qy, ry]]
    det = determinant3x3(arr)

    if det == 0:
        print('TOUCH')
    elif det < 0:
        print('RIGHT')
    else:
        print('LEFT')
