a,b = input().split()
a,b = int(a), int(b)

N = int(input())
if N == 0:
    print(0)
    exit()

intervale = [input().split() for _ in range(N)]
intervale = [(int(x[0]),int(x[1])) for x in intervale]

intervale.sort(key=lambda x: (x[0],x[1]))

selected = []
poz = 0

while poz < len(intervale) and a < b:
    intervselect = None
    selectpoz = None

    while poz < len(intervale) and intervale[poz][0] <= a:
        if intervselect is None:
            intervselect = intervale[poz]
            selectpoz = poz
        elif intervale[poz][1] >= intervselect[1]:
            intervselect = intervale[poz]
            selectpoz = poz
        poz += 1

    if intervselect is not None and selectpoz is not None:
        if intervselect[1] < a:
            break
        selected.append(selectpoz+1)
        a = intervselect[1]
    else:
        break


if len(selected) == 0 or intervale[selected[-1]-1][1] < b:
    print(0)
else:
    print(len(selected))
    for el in selected:
        print(el, end=' ')