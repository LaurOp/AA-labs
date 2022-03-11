def inp():
    n = input()
    
    quant = input().split(' ')
    quant = [int(x) for x in quant]
        
    val = input().split(' ')
    val = [int(x) for x in val]
    
    ratio = [val[i]/quant[i] for i in range(len(quant))]
    
    print(ratio)
    
    M = input()
    M = int(M)
    return n, quant, val, ratio, M

def maxRet(ls):
    m = ls[0]
    p = 0
    for i in range(len(ls)):
        if ls[i] > m:
            m = ls[i]
            p = i
    if p != len(ls)-1:
        ls = ls[:p] + ls[p+1:]
    else:
        ls = ls[:p]
    
    return m, p, ls
  
  
n, quant, val, ratio, M = inp()

def update(p):
    global quant
    global val
    if p != len(quant)-1:
        quant = quant[:p] + quant[p+1:]
        val = val[:p] + val[p+1:]
    else:
        quant = quant[:p]
        val = val[:p]

profit = 0
act, p, ratio = maxRet(ratio)

while M - quant[p] >= 0:
    print('Am luat complet cantitatea', quant[p], ', valoarea', val[p])
    M -= quant[p]
    update(p)
    profit += val[p]
    act, p, ratio = maxRet(ratio)
    
print('Am luat partial',M,'din', quant[p], ', valoarea', (M/quant[p])*val[p])
