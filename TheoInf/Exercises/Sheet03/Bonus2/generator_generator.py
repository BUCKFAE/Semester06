with open("Exercises/Sheet03/Bonus2/main.py") as f:
    lines = f.readlines()

    print(''.join(line.replace("    ", "\\t").replace("\n", "\\n") for line in lines))