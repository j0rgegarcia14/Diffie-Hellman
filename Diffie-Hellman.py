from random import randint


def Prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primitiveRoot(p):
    primitive_roots = []
    for g in range(2, p):
        powers = [pow(g, exp, p) for exp in range(1, p)]
        if len(set(powers)) == p - 1:
            primitive_roots.append(g)
    return primitive_roots[0]

p = randint(10, 1000)
while not Prime(p):
    p = randint(10, 1000)

g = primitiveRoot(p)
a = randint(2, p - 2)
b = randint(2, p - 2)
A = pow(g, a, p)
B = pow(g, b, p)
S_Alice = pow(B, a, p)
S_Bob = pow(A, b, p)

print("Prime Number: ", p)
print("Primitive Root: ", g)
print("Private Key for Alice: ", a)
print("Private Key for Bob: ", b)
print("Public Key for Alice: ", A)
print("Public Key for Bob: ", B)
print("Shared Secret for Alice:", S_Alice)
print("Shared Secret for Bob:", S_Bob)