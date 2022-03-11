from collections import defaultdict


# Recursiv. Foarte ineficient, O(2^n), O(1) spatiu. Nu poate rula pe numere mari
def fiboRecurs(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    return fiboRecurs(n - 1) + fiboRecurs(n - 2)


d = defaultdict()


# golden_ratio aprox 1.6
# O(golden_ratio ^ n) timp, O(n) memorie. Calculeaza doar o data fib(orice numar), dar tot intra in recursie pt toate
def fibo(n, dictionar):
    if n < 1:
        d[n] = 0
    if n == 1 or n == 2:
        d[n] = 1
    if n not in d:
        d[n] = fibo(n - 1, dictionar) + fibo(n - 2, dictionar)

    return d[n]


# Iterativul cere O(n) timp si O(1) memorie
def fiboIterativ(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b

    return b
