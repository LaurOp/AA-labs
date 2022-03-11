from collections import defaultdict
from pathlib import Path


# O(n) unde n = lungimea sirului; O(1) memorie; nr de caractere este aprox 255, deci neglijabil
def freq(strCh):
    frec = defaultdict()
    for c in strCh:
        if c in frec.keys():
            frec[c] += 1
        else:
            frec[c] = 1
    return frec


# print(freq("afsafgsa"))


# def minExcept(x, ls):
#     m2 = max(ls.values())
#     c = 1
#     lit = ''
#     for el in ls.keys():
#         if m2 == x:
#             c = 0
#         elif m2 >= ls[el]:
#             if ls[el] != x or c == 0:
#                 m2 = ls[el]
#                 lit = el
#
#     return lit, m2


# print(minExcept(2,freq("afsafgsa")))

class Node:  # structura de arbore; are si getteri
    def __init__(self, value, symb='', left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.symb = symb

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_value(self):
        return self.value

    def get_symb(self):
        return self.symb


def Huffman(frequencies):  # transforma dictionarul de frecvente in arbore Huffman
    # print('a)', frequencies)
    if len(frequencies) == 0:
        return None

    coada = [Node(frequencies[i], i) for i in frequencies.keys()]  # O(n^2) timp , O(n) memorie;
    # Se poate optimiza la O(n log n) prin heapify

    while len(coada) > 1:  # coada scade cu cate un element per iteratie => O(n)
        first = min(coada, key=lambda x: x.value)  # functie O(n)
        coada.remove(first)  # functie O(n)
        second = min(coada, key=lambda x: x.value)  # functie O(n)
        coada.remove(second)  # functie O(n)

        newNode = Node(first.value + second.value, first.symb + second.symb, first, second)

        coada.append(newNode)

    return coada[0]  # are doar un element


# O(n) pt ca se trece doar o data prin fiecare nod; O(n) memorie pt ca folosim un dictionar cu maxim n chei
def codificare(sir, arbore):
    codif = defaultdict()

    def parcurgere(arb, text=""):
        if arb is None:
            return ""
        elif arb.left is None and arb.right is None:
            codif[arb.symb] = text
        else:
            parcurgere(arb.left, text + "0")
            parcurgere(arb.right, text + "1")

    parcurgere(arbore)
    # print('c1)', codif)

    rez = ""
    for el in sir:
        rez += codif[el]

    # print('c2)', rez)
    return rez


# codificare("afsafgsa", Huffman(freq("afsafgsa")))
# codificare("AAAAAAAAAAAAAAABBBBBBBCCCCCCDDDDDDEEEEE", Huffman(freq("AAAAAAAAAAAAAAABBBBBBBCCCCCCDDDDDDEEEEE")))

huf = Huffman(freq("Huffman coding is a data compression algorithm."))
codat = codificare("Huffman coding is a data compression algorithm.", huf)


# Eficienta O(n) pt ca fiecare nod este vizitat exact o singura data,
# O(1) memorie pt ca printam direct pe ecran rezultatul; daca il salvam devenea O(n) memoria
def decodificare(sir, arbore):
    def parcurgere(arb, poz, text):
        if arb is None:
            return poz
        if arb.left is None and arb.right is None:
            print(arb.symb, end='')
            return poz

        arb = arb.left if text[poz + 1] == '0' else arb.right
        return parcurgere(arb, poz + 1, text)

    pozz = -1
    while pozz < len(sir) - 1:
        pozz = parcurgere(arbore, pozz, sir)


# print('d)', end=' ')
decodificare(codat, huf)

shakespeare = Path('shakespeare.txt').read_text()

hufShake = Huffman(freq(shakespeare))

f = open("shakeout.txt", "w")
f.write(codificare(shakespeare, hufShake))
f.close()
