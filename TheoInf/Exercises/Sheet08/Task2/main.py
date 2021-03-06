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
        
def neaKomplement(A):                   # liefert NEA, der das Komplement von L(A) akzeptiert,
    [Sigma, Z, delta, z0, F] = nea2dea(A)

    return dea2nea([Sigma, Z, delta, z0, Z - F])

def dea2nea(A):
    [Sigma, Z, delta, z0, F] = A

    newDelta = {}
    for key in delta:
        newDelta[key] = [delta[key]]

    return [Sigma, set(Z), newDelta, z0, set(F)]

def neaVereinigung(A,B):                # liefert NEA, der die Vereinigung von L(A) und L(B) akzeptiert,
    [Sigma, AZ, Adelta, Az0, AF] = A    # wobei A,B NEAs entsprechend Definition 3.12 sind
    [Sigma, BZ, Bdelta, Bz0, BF] = B
    
    # Zustandsmenge umbenennen
    AZ = [(1, z) for z in AZ]
    BZ = [(2, z) for z in BZ]

    # Startzustaende umbenennen
    Az0 = (1, Az0)
    Bz0 = (2, Bz0)

    # Startzustand für C
    Cz0 = 0

    # Akzeptierte Zustaende umbenennen
    AF = [(1, z) for z in AF]
    BF = [(2, z) for z in BF]
    CF = (AF + BF)

    if Az0 in AF or Bz0 in BF:
        CF += Cz0

    # Adelta anpassen
    newAdelta = {}
    for key in Adelta.keys():
        newAdelta[(1, key[0]), key[1]] = [(1, r) for r in Adelta[key]]

    # Bdelta anpassen
    newBdelta = {}
    for key in Bdelta.keys():
        newBdelta[(2, key[0]), key[1]] = [(2, r) for r in Bdelta[key]]

    # Überführungsfunktion
    Cdelta = newAdelta.copy()
    Cdelta.update(newBdelta)

    for a in Sigma:
        Cdelta[Cz0, a] = []

    # Neuer Startzustand nach A
    for key in newAdelta.keys():
        if key[0] == Az0:
            Cdelta[Cz0, key[1]] = Cdelta[Cz0, key[1]] + newAdelta[key]

    # Neuer Startzustand nach B
    for key in newBdelta.keys():
        if key[0] == Bz0:
            Cdelta[Cz0, key[1]] = Cdelta[Cz0, key[1]] + newBdelta[key]

    return [Sigma, set(AZ + BZ + [Cz0]), Cdelta, Cz0, set(CF)]
    
def neaKonkatenation(A,B):              # liefert NEA, der L(A)L(B) akzeptiert,
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

    # Startzustand von B akzeptiert -> Alle Endzustände von A auch akzeptiert
    if Bz0 in BF:
        BF += AF

    # Adelta anpassen
    newAdelta = {}
    for key in Adelta.keys():
        newAdelta[(1, key[0]), key[1]] = [(1, r) for r in Adelta[key]]

    # Bdelta anpassen
    newBdelta = {}
    for key in Bdelta.keys():
        newBdelta[(2, key[0]), key[1]] = [(2, r) for r in Bdelta[key]]

    # Überführungsfunktion
    Cdelta = newAdelta.copy()
    Cdelta.update(newBdelta)

    # Akzeptiert A -> B
    for z in AF:
        for a in Sigma:
            # Key Einfügen
            if (z, a) not in Cdelta.keys():
                Cdelta[z, a] = []
            # Überführung anpassen
            Cdelta[z, a] = Cdelta[z, a] + newBdelta[Bz0, a]

    return [Sigma, AZ + BZ, Cdelta, Az0, set(BF)]

def deaErweiterteUEF(delta, z, w):  # erweiterte ̈Uberf ̈uhrungsfunktion eines DEA
    for a in w:
        z = delta[z, a]
    return z
    
def deaRun(A, w):                   # testet, ob der DEA A das Wort w akzeptiert
    [Sigma, Z, delta, z0, F] = A
    return deaErweiterteUEF(delta, z0, w) in F 

def evalK(w):

    if w == '':
        return False
    
    if len(w) == 1 and w[0] == '1':
        return True

    if len(w) >= 2 and w[0] == '1' and w.count(1) == len(2) - 1 and w[-1] == '2':
        return True

    return False

def evalNotK(w):
    
    if w == '2' or w == '':
        return True

    if w.count('1') == len(w) and len(w) > 1:
        return True

    if '2' in w and w[-1] != 2:
        return True

    return False

def evalL(w):
    return w[0] == '1' and w[-1] == '2' if len(w) >= 2 else False

def evalNotL(w):

    if len(w) < 2:
        return True

    if w[0] != '1' or w[-1] != '2':
        return True

    return False

def evalM(w):
    return (w[-2] == '1' and len(w) >= 2) if len(w) > 1 else False

def evalNotM(w):
    if len(w) < 2:
        return True
    if w[-2] != '1':
        return True
    return False  

# Automaten aus Aufgabe 1
K = [{'1', '2'}, [0, 1, 2], {(0, '1'): [1, 2], (0, '2'): [], (1, '1'): [1], (1, '2'): [2], (2, '1'): [], (2, '2'): []}, 0, {2}]
L = [{'1', '2'}, [0, 1, 2], {(0, '1'): [1], (0, '2'): [], (1, '1'): [1], (1, '2'): [2], (2, '1'): [1], (2, '2'): [2]}, 0, {2}]
M = [{'1', '2'}, [0, 1, 2], {(0, '1'): [0, 1], (0, '2'): [0], (1, '1'): [1, 2], (1, '2'): [0, 2], (2, '1'): [], (2, '2'): []}, 0, {2}]

# Fälle zum Automaten testen
test_cases = [''] + [str(bin(i))[2:].replace("0", "tmp").replace("1", "2").replace("tmp", "1") for i in range(100)]

# Testet alle Testcases
for curr in test_cases:

    print(f"Word: \"{curr}\"")

    # Testet K, K-Komplement
    assert deaRun(nea2dea(K), curr) == evalK(curr)
    assert deaRun(nea2dea(neaKomplement(K)), curr) == evalNotK(curr)

    # Testet L, L-Komplement
    assert deaRun(nea2dea(L), curr) == evalL(curr)
    assert deaRun(nea2dea(neaKomplement(L)), curr) == evalNotL(curr)

    # Testet M, M-Komplement
    assert deaRun(nea2dea(M), curr) == evalM(curr)
    assert deaRun(nea2dea(neaKomplement(M)), curr) == evalNotM(curr)

    # Testet Vereinigung
    assert deaRun(nea2dea(neaVereinigung(K, L)), curr) == (evalK(curr) or evalL(curr))
    assert deaRun(nea2dea(neaVereinigung(L, K)), curr) == (evalK(curr) or evalL(curr))
    assert deaRun(nea2dea(neaVereinigung(K, M)), curr) == (evalK(curr) or evalM(curr))
    assert deaRun(nea2dea(neaVereinigung(L, K)), curr) == (evalL(curr) or evalK(curr))

    # Speichert ob Konkatenation curr akzeptiert
    concat_K_K = False
    concat_L_L = False
    concat_M_M = False
    concat_L_M = False
    concat_L_U_M_N_K = False

    # Testet ob Konkatenation curr akzeptiert
    for bound in range(len(curr) + 1):

        # Wort aufteilen
        part1 = curr[:bound]
        part2 = curr[bound:]

        # Testen ob die aktuelle Kombination valide ist
        concat_K_K = True if evalK(part1) and evalK(part2) else concat_K_K
        concat_L_L = True if evalL(part1) and evalL(part2) else concat_L_L
        concat_M_M = True if evalM(part1) and evalM(part2) else concat_M_M
        concat_L_M = True if evalL(part1) and evalM(part2) else concat_L_M

        concat_L_U_M_N_K = True if (((evalL(part1) or evalM(part1))) and (evalNotK(part2))) else concat_L_U_M_N_K

    # Testet Konkatenation
    assert deaRun(nea2dea(neaKonkatenation(K, K)), curr) == concat_K_K
    assert deaRun(nea2dea(neaKonkatenation(L, L)), curr) == concat_L_L
    assert deaRun(nea2dea(neaKonkatenation(M, M)), curr) == concat_M_M
    assert deaRun(nea2dea(neaKonkatenation(L, M)), curr) == concat_L_M

    # Testet (L or M) and (not K)
    assert deaRun(nea2dea(neaKonkatenation(neaVereinigung(L, M), neaKomplement(K))), curr) == concat_L_U_M_N_K

    