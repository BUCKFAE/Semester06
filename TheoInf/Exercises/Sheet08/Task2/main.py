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

            for z in S:
                print(f"z: {z}")

                print(f"delta[{z}, {a}] = {delta[z, a]}")
                for s in delta[z, a]:
                    print(f"s: {s}")

            delta1[S,a] = frozenset({s for z in S for s in delta[z, a]})

    F1 = {S for S in Z1 if (S & F) != set()}
    return [Sigma, Z1, delta1, frozenset({z0}), F1]
        

def dea2nea(A):
    [Sigma, Z, delta, z0, F] = A 
    NZ = [[z] for z in Z]
    NF = [[f] for f in F]

    return [Sigma, NZ, delta, [z0], NF]

def neaKomplement(A):                   # liefert NEA, der das Komplement von L(A) akzeptiert,
    [Sigma, Z, delta, z0, F] = A        # wobei A ein NEA entsprechend Definition 3.12 ist

    return [Sigma, Z, delta, z0, [z for z in Z if z not in F]]
    
def neaVereinigung(A,B):                # liefert NEA, der die Vereinigung von L(A) und L(B) akzeptiert,
    [Sigma, AZ, Adelta, Az0, AF] = A    # wobei A,B NEAs entsprechend Definition 3.12 sind
    [Sigma, BZ, Bdelta, Bz0, BF] = B
    
    # Zustandsmenge umbenennen
    AZ = [(1, z) for z in AZ]
    BZ = [(2, z) for z in BZ]

    # Startzustaende umbenennen
    Az0 = (1, Az0)
    Bz0 = (2, Bz0)

    # Akzeptierte Zustaende umbenennen
    AF = [(1, z) for z in AF]
    BF = [(2, z) for z in BF]

    # Adelta anpassen
    newAdelta = {}
    for key in Adelta.keys():
        newAdelta[((1, key[0]), key[1])] = (1, Adelta[key])

    # Bdelta anpassen
    newBdelta = {}
    for key in Bdelta.keys():
        newBdelta[((2, key[0]), key[1])] = (2, Bdelta[key])

    # Startzustand für C
    Cz0 = 0

    # Überführungsfunktion
    Cdelta = {}

    print(f"Adelta: {newAdelta}")
    print(f"Bdelta: {newBdelta}")

    sum = newAdelta.copy()
    sum.update(newBdelta)

    print(f"Sum: {sum}")

    print(f"Az0: {Az0}")
    print(f"Bz0: {Bz0}")

    CF = (AF + BF)

    # Alten Überführungsfunktionen übernehmen
    for key in sum.keys():
        Cdelta[key] = sum[key]

        # TODO: Leeres Wort!!

        print(f"{key} -> {Cdelta[key]}")
        if key[0] == Az0 or key[0] == Bz0:
            Cdelta[(Cz0, key[1])] = Cdelta[key]
            print(f"Start: {(Cz0, key[1])} -> {Cdelta[(Cz0, key[1])]}")


    C = [Sigma, AZ + BZ, Cdelta, Cz0, CF]

    return C
    
def neaKonkatenation(A,B):              # liefert NEA, der L(A)L(B) akzeptiert,
    [Sigma, AZ, Adelta, Az0, AF] = A    # wobei A,B NEAs entsprechend Definition 3.12 sind
    [Sigma, BZ, Bdelta, Bz0, BF] = B

    # TODO
    C = None

    return C

def deaErweiterteUEF(delta, z, w):  # erweiterte ̈Uberf ̈uhrungsfunktion eines DEA
    for a in w:
        z = delta[z, a]

    print(f"Stopped: {z}")
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

def printDEA(A):
    [Sigma, Z, delta, z0, F] = A
    print(f"Sigma: {Sigma}")
    print(f"Z:     {Z}")
    print(f"Delta: {delta}")
    print(f"Start: {z0}")
    print(f"F:     {F}")

a1 = dea2nea(createFastSearchDEA({'0', '1'}, '0'))
a2 = dea2nea(createFastSearchDEA({'0', '1'}, '1'))

a1_n = neaKomplement(a1)
print(f"NEA 1:\n{a1}\nKomplement:\n{a1_n}")

print("\n\n--------------\n\n")

a1_a2_cup = neaVereinigung(a1, a2)
print(f"NEA 1:\n{a1}\nNEA 1:\n{a2}\nVereinigung:\n{a1_a2_cup}")

printDEA(a1_a2_cup)

print(nea2dea(deaRun(a1_a2_cup, '1')))
print(nea2dea(deaRun(a1_a2_cup, '0')))
print(nea2dea(deaRun(a1_a2_cup, '11')))
print(nea2dea(deaRun(a1_a2_cup, '00')))

# TODO: Leeres Wort!!!
print("\n\n--------------\n\n")
