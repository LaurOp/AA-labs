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


def intersectie(orizontale, verticale, punct):
    # vom memora capetele impuse de plane
    st, dr, sus, jos = float('-inf'), float('inf'), float('inf'), float('-inf')
    xCoord = punct[0]
    yCoord = punct[1]

    # parcurgem intai planele verticale
    for (x, val) in verticale:
        if x > 0:  # x <= -val
            val /= (-x)
            if val > xCoord:
                dr = min(val, dr)
        else:  # -x >= val
            val /= (-x)
            if val < xCoord:
                st = max(val, st)

        # oprim codul daca dr < st , pt ca intersectia va fi vida sigur
        if dr < st:
            return "VOID"
    else:
        # facem acelasi lucru si cu orizontalele
        for (y, val) in orizontale:
            if y > 0:  # y <= -val
                val /= (-y)
                if val > yCoord:
                    sus = min(val, sus)
            else:  # y >= -val
                val /= (-y)
                if val < yCoord:
                    jos = max(val, jos)

            # oprim codul daca sus < jos , pt ca intersectia va fi vida sigur
            if sus < jos:
                return "VOID"

        else:
            # daca intersectia nu e vida dar are un capat infinit, este UNBOUNDED
            if float('inf') in [st, dr, jos, sus] or float('-inf') in [st, dr, jos, sus]:
                return "FULLY_UNBOUNDED"
            else:
                return st, dr, jos, sus


for punct in puncte:
    raspuns = intersectie(orizontale, verticale, punct)

    if raspuns in ["VOID", "FULLY_UNBOUNDED"]:
        print("NO")
    else:
        st, dr, jos, sus = raspuns
        print("YES")
        print(round((dr-st) * (sus-jos), 6))

