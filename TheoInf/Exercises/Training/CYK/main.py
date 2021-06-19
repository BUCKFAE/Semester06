def CYK(w, rules):
    
    if len(w) == 0: return 0

    tables = {}

    # Creating tables
    for key, item in rules:
        # Filling table with zeros
        if key not in tables.keys(): tables[key] = [len(w) * [0] for _ in range(len(w))]

        # Skipping if rule is not A -> a
        if len(item) == 2: continue

        # Filling Table if A -> ai is a rule
        for i in range(len(w)):
            if w[i] == item: 
                tables[key][i][i] = 1

    # Iterating possibilities
    for k in range(1, len(w)):
        for i in range(0, len(w) - k):
            for j in range(i, i + k):

                # Iterating over rules
                for key, item in rules:

                    # Skipping if rule is not A -> BC
                    if len(item) == 1: continue

                    # if B[i][j] == 1 and C[j + 1][i + k] == 1: A[i][i + k] = 1
                    if tables[item[0]][i][j] == 1:
                        if tables[item[1]][j + 1][i + k] == 1:
                            tables[key][i][i + k] = 1

    # Returning the result
    return tables["S"][0][len(w) - 1]

# Testing
rules = [("S", "CA"), ("A", "CA"), ("B", "AC"), ("C", "BA"), ("A", "a"), ("B", "b"), ("C", "b")]
w1 = "abbaa"
w2 = "abba"

print(f"Result: {CYK(w1, rules)}")
print(f"Result: {CYK(w2, rules)}")