def powerset(s):                        # liefert die Potenzmenge der Menge s
    ps = {frozenset()}                  # Verwendung von frozenset statt set, da Mengen nur
    for z in s:                         # nichtver ̈anderbare Objekte enthalten d ̈urfen. Beispiel:
        ps |= {a | {z} for a in ps}     #     falsch:  a = { {1,2}, {4,5} }
    return ps                           #     richtig: a = { frozenset({1,2}), frozenset({4,5}) }
    
def nea2dea(A):                         # liefert  ̈aquivalenten DEA (Potenzmengenkonstruktion)
    [Sigma, Z, delta, z0, F] = A        # A ist ein NEA entsprechend Definition 3.12
    Z1 = powerset(Z)
    delta1 = {}                         # ̈Uberf ̈uhrungsfunktion
    for S in Z1:                        # Verwendung von frozenset statt set, da Mengen nur
        for a in Sigma:                 # nichtver ̈anderbare Objekte enthalten d ̈urfen.
            delta1[S,a] = frozenset({s for z in S for s in delta[z, a]})
    


    F1 = {S for S in Z1 if (S & F) != set()}
    return [Sigma, Z1, delta1, frozenset({z0}), F1]

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

def dea2nea(A):
    [Sigma, Z, delta, z0, F] = A

    newDelta = {}
    for key in delta.keys():
        newDelta[key] = [delta[key]]

    return [Sigma, Z, newDelta, z0, set([f for f in F])]

# DEA testing for 122
a_1 = createFastSearchDEA({'1', '2'}, '122')
print(f"DEA A1: {a_1}")
print("\n".join([f"{i} -> {deaRun(a_1, i)}" for i in ['1', '2', '122', '121', '2122', '21221']]))

# DEA -> NEA -> DEA
a_1_r = nea2dea(dea2nea(a_1))
print(f"DEA A1: {a_1_r}")
print("\n".join([f"{i} -> {deaRun(a_1_r, i)}" for i in ['1', '2', '122', '121', '2122', '21221']]))

# NEA 
Sigma = {'1', '2'}
Z = [0, 1, 2]
delta = {(0, '1'): [1, 2], (0, '2'): [], (1, '1'): [1], (1, '2'): [2], (2, '1'): [], (2, '2'): []}
z0 = 0
F = {2}
a_1_copy = [Sigma, Z, delta, z0, F]
a_1_nea = nea2dea(a_1_copy)

print(f"NEA A1: {a_1_nea}")
print("\n".join([f"{i} -> {deaRun(a_1_nea, i)}" for i in ['1', '2', '122', '121', '2122', '21221']]))