n = int(input())

puncte = []

for _ in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    puncte.append((x, y))


# functie ce compara 2 pozitii dintr-un array si verifica daca sunt in ordine crescatoare
# daca sunt egale, compara indecsii , ce ar trebui sa fie in ordine crescatoare
def inorder(arr, i, j, poz):
    return (arr[i][poz] < arr[j][poz]) or (arr[i][poz] == arr[j][poz] and i < j)


# numarul de minime locale
minimeX = 0

# Rezolvarea merge pe ideea ca intr-un poligon monoton UN SINGUR punct este mai mic (relativ la directie x sau y)
# decat ambii sai vecini in caz contrar nu este monoton

# X-Monotonie
for i in range(n):
    if inorder(puncte, i, (i + 1) % n, 0) and inorder(puncte, i, i - 1, 0):
        minimeX += 1

if minimeX == 1:
    print("YES")
else:
    print("NO")


# Y-Monotonie
minimeY = 0
for i in range(n):
    if inorder(puncte, i, (i + 1) % n, 1) and inorder(puncte, i, i - 1, 1):
        minimeY += 1

if minimeY == 1:
    print("YES")
else:
    print("NO")
