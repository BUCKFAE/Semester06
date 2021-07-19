pflichtbereich = {
    "ADS": [2.3, 10],
    "GDP": [1.7, 5],
    "HWP": [None, 10],
    "RIU": [1.0, 10],
    "LGK": [2.7, 5],
    "MA1": [3.0, 10],
    "MA2": [3.3, 10],
    "JPP": [None, 10],
    "REA": [3.0, 10],
    "SWP": [None, 10],
    "SWT": [2.3, 10]}

wahlpflichtbereich = {
    "DBS": [3.0, 5],
    "WIN": [3.0, 5],
    "AVP": [2.3, 5]}

semiare = {
    "ASQ": [None, 5],
    "SE1": [1.3, 5],
    "SE2": [1.3, 5]}

def ects(d):
    return sum(d[k][1] for k in d)

def grade(d):
    return round_to(sum([(d[k][0] if d[k][0] is not None else 0) * d[k][1] for k in d]) / sum(d[k][1] if d[k][0] is not None else 0 for k in d))

def round_to(d):
    g = [1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0]
    return min(g, key=lambda a: abs(a - d))

# All grades in one dict
all = {}
all.update(pflichtbereich)
all.update(wahlpflichtbereich)
all.update(semiare)

print(f"\nPFLICHT:\nECTS: {ects(pflichtbereich)}, GRADE: {grade(pflichtbereich)}")
print(f"\nWAHLPFLICHT:\nECTS: {ects(wahlpflichtbereich)}, GRADE: {grade(wahlpflichtbereich)}")
print(f"\nSEMINARE:\nECTS: {ects(semiare)}, GRADE: {grade(semiare)}")

print(f"\nTOTAL:\nECTS: {ects(all)}, GRADE: {round((grade(pflichtbereich) + grade(wahlpflichtbereich) + grade(semiare)) / 3, 1)}")


# Calculating if i only score 4.0
worst_possible = {}
for i in range(0, 180 - ects(all), 5):
    worst_possible[str(i)] = [4.0, 5]
all.update(worst_possible)

print(f"\nWORST POSSIBLE:\nECTS: {ects(all)}, GRADE: {round((grade(pflichtbereich) + grade(wahlpflichtbereich) + grade(semiare) + grade(worst_possible)) / 4, 1)}")
