def run(word):

    states = ["0"]
    stacks = [["s"]]

    # X needs to be replaced by e, A, B
    rules = {
        "0aX": "0AX",
        "0bX": "0BX",
        "0aX": "1eX",
        "0bX": "1eX",
        "0eX": "1eX",
        "1aA": "1es",
        "1bB": "1es",
        "1sd": "1es"
    }

    # Iterating over the word
    for c in word:
        
        print(f"Current char: {c}")

        newStates = []
        newStacks = []

        for currentState in range(len(states)):

            print(f"State: {currentState}")

            for rule in rules.keys():
                print(f"\n\nCurrent rule: {rule} -> {rules[rule]}")

                for currentRule in set([(rule.replace("X", r), rules[rule].replace("X", r)) for r in ["s", "A", "B"]]):
                    print(f"Rule adjusted: {currentRule}")

                    print(f"{states[currentState]=} == {currentRule[0][0]=}")
                    if states[currentState] == currentRule[0][0]:
                        print(f"{c=} == {currentRule[0][1]=}")
                        if c == currentRule[0][1]:

                            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

                            print(f"{stacks[currentState]=} == {currentRule[0][2]=}")
                            if stacks[currentState] == currentRule[0][2]:
                                
                                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                                newStates.append(currentRule[1][0])

                                currentStack = stacks[currentState]
                                currentStack, _ = pop(currentStack)
                                push(currentStack, currentRule[1][1])
                                push(currentStack, currentRule[1][2])
                                newStacks.append(currentStack)



        stacks = newStacks
        states = newStates

    print(f"{stacks=}")
    print(f"{states=}")

    return any([len(s) == 0 or (len(set(s)) == 1 and s[0] == "s") for s in stacks])
                


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

print(f"{run('abba')=}")
#print(f"{run('abaa')=}")