"""Getting the dyadic representation from a base 10 number

109 = 2 * 54 + 1
 54 = 2 * 26 + 2
 26 = 2 * 12 + 2
 12 = 2 *  5 + 2
  5 = 2 *  2 + 1
  2 = 2 *  0 + 2

We can get the next starting number by using
x = (x - 1) // 2 

We use number ** (1/2) as upper bound
"""

number = 109

nums = [i for i in range(int(number ** (1/2)))]


#exp = '('*8 + '(109 - 1 // 2)' + ''.join([" - 1) // 2)".format(number) for i in range(4)])
#print(exp)

def to_dya(x):
    expressions = [eval("(" * (i * 2) + "({} - 1 // 2)".format(x) + "".join([" - 1) // 2)" for j in range(i)])) for i in range(int(x ** (1 / 2) + 1))]

    #return [r for r in [None if i <= 0 else (1 if i % 2 == 1 else 2) for i in expressions[::-1]] if r is not None]

    return [r for r in [None if i <= 0 else (1 if i % 2 == 1 else 2) for i in [eval("(" * (i * 2) + "({} - 1 // 2)".format(x) + "".join([" - 1) // 2)" for j in range(i)])) for i in range(int(x ** (1 / 2) + 1))][::-1]] if r is not None]


print(to_dya(1))
print(to_dya(2))
print(to_dya(3))
print(to_dya(109))