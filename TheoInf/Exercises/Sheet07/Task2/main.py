def deaDefine():                    # definiert einen DEA A
    Sigma = {'0', '1'}              # Alphabet
    Z = {0, 1, 2}                   # Zustandsmenge
    delta = {}                      # ̈Uberf ̈uhrungsfunktion
    delta[0,'0'] = 1
    delta[0,'1'] = 0
    delta[1,'0'] = 1
    delta[1,'1'] = 2
    delta[2,'0'] = 2
    delta[2,'1'] = 2
    
    F = {2}                         # Menge der akzeptierenden Zust ̈ande
    
    A = [Sigma, Z, delta, 0, F]
    
    return A
    
def deaErweiterteUEF(delta, z, w):  # erweiterte ̈Uberf ̈uhrungsfunktion eines DEA
    for a in w:
        z = delta[z, a]

    return z
    
def deaRun(A, w):                   # testet, ob der DEA A das Wort w akzeptiert
    [Sigma, Z, delta, z0, F] = A
    
    return deaErweiterteUEF(delta, z0, w) in F 


def createFastSearchDEA(Sigma, v):

    Z = set([i for i in range(len(v) + 1)])
    F = {len(v)}

    delta = {}

    # Iterating over the index of all chars
    for i in range(len(v)):
        
        print(f"i: {i}")

        # Next char matches
        delta[i, v[i]] = i + 1

        # Cases that don't match
        for s in Sigma:

            if s == v[i]:
                continue

            delta[i, s] = findBiggestMatch(v, v[:i - 2] + s)


    # Stay accepted
    for s in Sigma:
        delta[len(v), s] = len(v)

    return [Sigma, Z, delta, 0, F]

def findBiggestMatch(v, w):

    biggest = 1

    while w.endswith(v[:biggest]) and biggest < len(v):
        biggest += 1

    biggest -= 1

    return biggest


A = deaDefine()
print(A)
print(deaRun(A, '11100011'))

fast = createFastSearchDEA({'0', '1'}, '101')
print(fast)
print(deaRun(fast, '10110'))
print(deaRun(fast, '10010'))
print(deaRun(fast, '110010100'))

A = {1: 0, 2: 9}
A.