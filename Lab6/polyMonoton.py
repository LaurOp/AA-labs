n = int(input())

puncte = []

for _ in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    puncte.append((x, y))


def inorder(arr, i, j, poz):
    return (arr[i][poz] < arr[j][poz]) or (arr[i][poz] == arr[j][poz] and i < j)


minimeX = 0
for i in range(n):
    if inorder(puncte, i, (i + 1) % n, 0) and inorder(puncte, i, i - 1, 0):
        minimeX += 1

if minimeX == 1:
    print("YES")
else:
    print("NO")


minimeY = 0
for i in range(n):
    if inorder(puncte, i, (i + 1) % n, 1) and inorder(puncte, i, i - 1, 1):
        minimeY += 1

if minimeY == 1:
    print("YES")
else:
    print("NO")


