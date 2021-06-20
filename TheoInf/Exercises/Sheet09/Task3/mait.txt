# gibt alle Paare von unterscheidbaren Zustaenden in A zurueck
def deaUnterscheidbareZustaende(A):
    [Sigma, Z, delta, z0, F] = A
    
    # Speichert markierte Zustände
    markiert = []

    veraendert = True

    while veraendert:

        veraendert = False

        # Pruefen ob eintrag zur Tabelle hinzugefuegt werden kann
        for z1 in Z:
            for z2 in Z:

                # Naechstes paar falls aktuelles paar schon behandelt
                if z1 == z2 or {z1, z2} in markiert:
                    continue

                # Unterschiedliches Akzeptierungsverhalten
                if (z1 in F) ^ (z2 in F):
                    markiert.append({z1, z2})
                    veraendert = True

                # Pruefen ob man ueber a zu bereits markiertem paar kommt
                for a in Sigma:
                    rz1 = delta[z1, a]
                    rz2 = delta[z2, a]

                    # Neues paar ist markeirt
                    if {rz1, rz2} in markiert:
                        markiert.append({z1, z2})
                        veraendert = True

    return markiert

def deasAequivalent(A, B):   # prueft, ob DEAs A und B die gleiche Sprache akzeptieren
    [ASigma, AZ, Adelta, Az0, AF] = A
    [BSigma, BZ, Bdelta, Bz0, BF] = B

    Sigma = ASigma & BSigma  # Annahme: ASigma = BSigma

    Z = AZ + BZ

    delta = Adelta.copy()
    delta.update(Bdelta)

    F = AF + BF
    C = [Sigma, Z, delta, Az0, F]

    return {Az0, Bz0} not in deaUnterscheidbareZustaende(C)

# Automaten aus Aufgabe 2
A1 = [{'a', 'b', 'c'}, [1, 2, 3], {(1, 'a'): 2, (1, 'b'): 2, (1, 'c'): 2, (2, 'a'): 3, (2, 'b'): 3, (2, 'c'): 3, (3, 'a'): 1, (3, 'b'): 1, (3, 'c'): 1}, 1, [1]]
A2 = [{'a', 'b', 'c'}, [4, 5, 6, 7, 8], {(4, 'a'): 7, (4, 'b'): 6, (4, 'c'): 7, (5, 'a'): 4, (5, 'b'): 4, (5, 'c'): 4, (6, 'a'): 5, (6, 'b'): 8, (6, 'c'): 5, (7, 'a'): 8, (7, 'b'): 8, (7, 'c'): 5, (8, 'a'): 4, (8, 'b'): 4, (8, 'c'): 4}, 4, [4]]

# A1, aber von (2, b) -> 1 statt nach 3
A3 = [{'a', 'b', 'c'}, [10, 20, 30], {(10, 'a'): 20, (10, 'b'): 20, (10, 'c'): 20, (20, 'a'): 30, (20, 'b'): 10, (20, 'c'): 30, (30, 'a'): 10, (30, 'b'): 10, (30, 'c'): 10}, 10, [10]]

# Gleicher Automat
assert deasAequivalent(A1, A1) == True
assert deasAequivalent(A2, A2) == True
assert deasAequivalent(A3, A3) == True

# Unterschiedlicher Automat
assert deasAequivalent(A1, A2) == True
assert deasAequivalent(A2, A1) == True
assert deasAequivalent(A1, A3) == False
assert deasAequivalent(A3, A1) == False
assert deasAequivalent(A2, A3) == False
assert deasAequivalent(A3, A2) == False

