human = "KKASKPKKAASKAPTKKPKATPVKKAKKKLAATPKKAKKPKTVKAKPVKASKPKKAKPVK"
cow = "KKAAKPKKAASKAPSKKPKATPVKKAKKKPAATPKKTKKPKTVKAKPVKASKPKKTKPVK"

rez = []


# Brute-force genereaza toate subsecventele ; O(2^n) timp, O(2^n) memorie;
def genSecvente(sir, poz=0, seq=""):
    if poz == len(sir):
        global rez
        rez.append(seq)
    else:
        genSecvente(sir, poz + 1, seq)
        genSecvente(sir, poz + 1, seq + sir[poz])


def bruteSubsequences(a, b):
    genSecvente(a)
    r1 = rez.copy()
    rez.clear()
    r1.sort(key=lambda x: -len(x))

    genSecvente(b)
    r2 = rez.copy()

    for el in r1:
        if el in r2:
            return len(el)

    return 0


print(bruteSubsequences("ABCDD", "DDABCE"))

# Cel mai eficient pt lungime 1 este un not bitwise-and pe codul ascii al caracterelor
# Este mai bine implementat in C decat in Py; acolo s-ar fi intors 1 in loc de true
def subsecvLen1(a, b) -> bool:
    return not (a ^ b)


print(subsecvLen1(ord('a'), ord('b')))


# O(n)
def subsecvLen1n(a, b):
    for ch in b:
        if a == ch:
            return 1
    return 0


print(subsecvLen1n('a', 'bsaftgedh'))


# O(n*m) timp; O(n*m) memorie;  le 1-indexam
def maxSubsequence(a, b):
    lungimi = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                lungimi[i][j] = lungimi[i - 1][j - 1] + 1
            else:
                lungimi[i][j] = max(lungimi[i - 1][j], lungimi[i][j - 1])

    return lungimi[-1][-1]


print(maxSubsequence(human, cow))
