"""Apriori Algorithm"""

data = [
    ["Bier", "Chips", "Windeln"],
    ["Bier", "Pizza"],
    ["Bier", "Chips", "Pizza"],
    ["Bier", "Cola", "Windeln"],
    ["Chips", "Cola"],
    ["Chips", "Cola", "Pizza"], 
    ["Bier", "Cola", "Windeln"],
    ["Chips", "Pizza"]
]

minsup = 0.25

I = list(set([i for s in data for i in s]))

def get_support(D, X):
    return sum([1 if all([x in d for x in X]) else 0 for d in D]) / len(D)

def apriori(I, D, minsup):

    L = [[[i] for i in I if get_support(D, [i]) > minsup]]
    k = 1

    while L[k - 1]:

        CK = genearate_apriori_candidates(L[k - 1])

        # Stores how often what set occured
        count = {}

        # Filling count dict
        for c in CK:
            if frozenset(c) not in count:
                count[frozenset(c)] = 0

        for T in D:
            CT = [k for k in CK if all([s in T for s in k])]

            for c in CT:
                count[frozenset(c)] = count[frozenset(c)] + 1

        L.append([c for c in CK if (count[frozenset(c)] / len(D) >= minsup)])
        k += 1

    return L[:-1]

def genearate_apriori_candidates(L):

    k = len(L[0]) - 1

    res = []

    # Step 1: Join
    for p in L:
        for q in L:
            if p[:k] == q[:k] and q != p:

                n = sorted(p + q[k:])
                if n not in res and len(set(n)) == len(n): res.append(n)

    # Step 2: Pruning
    for p in res:
        subsets = [p[:i] + p[i + 1:] for i in range(len(p))]
        if any([s not in L for s in subsets]):
            res.remove(p)

    return res


# Testing apriori candidate generation
test_data = [[1, 2, 3], [1, 2, 4], [1, 3, 4], [1, 3, 5], [2, 3, 4]]
print(f"Apriori Candidates:\n{test_data} -> {genearate_apriori_candidates(test_data)}")

res = apriori(I, data, minsup)
print(f"\n\nApriori given data:\n{res}")