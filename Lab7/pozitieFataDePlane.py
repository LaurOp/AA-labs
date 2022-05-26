n = int(input())

# vom separa planele dupa orientare: orizontale si verticale
orizontale = []
verticale = []

# citire
for _ in range(n):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    if a == 0:
        orizontale.append((b, c))  # introducem doar valorile nenule; pt orizontale y si pt verticale x
    else:
        verticale.append((a, c))

m = int(input())
puncte = []

for _ in range(m):
    point = input().split()
    puncte.append((float(point[0]), float(point[1])))


def intersectie(orizontale, verticale):
    # vom memora capetele impuse de plane
    st, dr, sus, jos = float('-inf'), float('inf'), float('inf'), float('-inf')

    # parcurgem intai planele verticale
    for (x, val) in verticale:
        if x > 0:  # x <= -val
            val /= (-x)
            dr = min(val, dr)
        else:  # -x >= val
            val /= (-x)
            st = max(val, st)

        # oprim codul daca dr < st , pt ca intersectia va fi vida sigur
        if dr < st:
            return "VOID"
    else:
        # facem acelasi lucru si cu orizontalele
        for (y, val) in orizontale:
            if y > 0:  # y <= -val
                val /= (-y)
                sus = min(val, sus)
            else:  # y >= -val
                val /= (-y)
                jos = max(val, jos)

            # oprim codul daca sus < jos , pt ca intersectia va fi vida sigur
            if sus < jos:
                return "VOID"

        else:
            # daca intersectia nu e vida dar are un capat infinit, este UNBOUNDED
            if float('inf') in [st, dr, jos, sus] or float('-inf') in [st, dr, jos, sus]:
                return "UNBOUNDED"
            else:
                return "BOUNDED", (st, dr, jos, sus)


raspuns = intersectie(orizontale, verticale)

if raspuns in ["VOID", "UNBOUNDED"]:
    for _ in range(m):
        print("NO")
else:
    pass

