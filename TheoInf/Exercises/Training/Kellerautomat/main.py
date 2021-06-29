from typing import SupportsRound


def run(word):
    """Runs the pda
    
    e -> epsilon
    t -> top symbol 
    """
    states = ["0"]
    stacks = [["t"]]

    # X needs to be replaced by e, A, B
    rules = {
        "0aX": "0AX",
        "0bX": "0BX",
        "0aX": "1X",
        "0bX": "1X",
        "0eX": "1X",
        "1aA": "1",
        "1bB": "1",
        "1et": "1"
    }

    # Iterating over the word
    for c in word:
        print(f"{stacks=}\n{states=}")

        states, stacks, _ = execute_rules(states, stacks, c, rules)

    print("Finished the word!")

    changed = True
    while changed and not  any([len(s) == 0 or (s.count("t") == len(s)) for s in stacks]):
        states, stacks, changed = execute_rules(states, stacks, None, rules)
        print(f"{stacks=}\n{states=}")


    print(f"{stacks=}\n{states=}")

    return any([len(s) == 0 or (len(set(s)) == 1 and s[0] == "t") for s in stacks])

def execute_rules(states, stacks, c, rules):

    newStates = []
    newStacks = []
    changed = False

    # Stepping for each state we are in right now
    for currentState in range(len(states)):

        newStacks.append(stacks[currentState])
        newStates.append(states[currentState])

        # Applying all rules
        for rule in rules.keys():

            # Exchaning X for t, A, B
            for currentRule in set([(rule.replace("X", r), rules[rule].replace("X", r)) for r in ["t", "A", "B"]]):

                # Checking if we are in the correct start state
                if states[currentState] == currentRule[0][0]:

                    # Checking if the input symbol matches
                    if c == currentRule[0][1] or currentRule[0][1] == "e":

                        if len(stacks[currentState]) == 0:
       
                            continue

                        # Checking if the symbol in sthe stack matches
                        if stacks[currentState][-1] == currentRule[0][2]:
                                
                            # Removing old 
                            newStacks.pop()
                            newStates.pop()

                            # Appending new state
                            newStates.append(currentRule[1][0])

                            currentStack = stacks[currentState].copy()
                            currentStack, _ = pop(currentStack)

                            for f in currentRule[1][1:]:
                                
                                currentStack = push(currentStack, f)


                            newStacks.append(currentStack)

                            changed = True

       

    return newStates.copy(), newStacks.copy(), changed                 


def push(stack, w):
    return stack + [w]

def pop(stack):
    if len(stack) > 0:
        return stack[:-1], stack[-1]
    return None

def is_symmetric(word):
    if len(word) % 2 == 0:
        return word == word[::-1]
    return is_symmetric(word[:int(len(word) / 2)] + word[int(len(word) / 2) + 1:])

# Testing if the stack works
stack = []
for i in range(10):
    stack = push(stack, i)

print(stack)
for i in range(9, -1, -1):
    stack, res = pop(stack)
    print(f"{stack=}\n{res=}\n{i=}")
    assert res == i

# Ensuring is_symmetric is correct
assert is_symmetric("a") == True
assert is_symmetric("b") == True
assert is_symmetric("ab") == False
assert is_symmetric("ba") == False
assert is_symmetric("aaa") == True
assert is_symmetric("bbb") == True
assert is_symmetric("aba") == True
assert is_symmetric("bab") == True
assert is_symmetric("bba") == False
assert is_symmetric("baa") == False

print(f"{run('aabaa')=}")
print(f"{run('abaa')=}")

#print(f"{run('abaa')=}")