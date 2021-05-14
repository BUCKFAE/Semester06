# Klaus Biehler, Johannes Jungkunst, Philipp Wahl

#Der algo verwendet die Idde der Zusatzaufgabe01 von Blatt02 (Siehe dafür Übungsvideo)
#Wir bestimmen die bits von a von rechts nach links und addieren gegebenenfalls + b auf das result
#Durch das verdoppeln des results wird diese +b letztendlich auch an die korrekte Stelle geshifted
#Laufzeit:
#Die erste while-Scheife läuft |a| mal durch.
#Da danach e = |a|, wird die zweite Schleife ebenfalls |a| mal durchlaufen
#Da das innere der Schleifen in konstanter Zeit läuft, ergibt sich eine Laufzeit von O(|a|), also auch O(|a|+|b|)=O(n)
def prodZ(a, b):

    print("A: {} {}".format(a, str(bin(a))[2:]))
    print("B: {} {}".format(b, str(bin(b))[2:]))

    if(a < 0):
        a = (0 - a)
        b = (0 - b)

    res = 0
    i = 1
    e = 1

    while((i + i) <= a): #Nach dieser Schleife ist e = |a| (falls a!=0)
        i = (i + i)
        e = (e + 1)

    print("Lower bound: {}".format(str(bin(i))[2:]))
    print("Length of A: {}".format(e))

    while(e > 0):

        print("\n---RES---")
        res = (res + res)
        print("Res: {}".format(str(bin(res))[2:]))
        print("---RES---\n")

        # Wenn a größer ist als die untere schranke
        if(a >= i): #True, falls das e-te bit von rechts > 0
            print("\n---IF---")
            print("A: {} {}".format(a, str(bin(a))[2:]))
            print("I: {} {}".format(i, str(bin(i))[2:]))
            a = (a - i)
            print("A: {} {}".format(a, str(bin(a))[2:]))
            res = (res + b)
            print("Res: {}".format(str(bin(res))[2:]))
            print("---IF---\n")

        # Restoring a
        print("A: {} {}".format(a, str(bin(a))[2:]))
        a = (a + a)
        print("A: {} {}".format(a, str(bin(a))[2:]))


        # We covered the
        e = (e - 1)
    return res