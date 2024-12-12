
elements = [item for item in range(100)]

def F(x, p):
    if x == 0:
        return 0
    else:
        c = x % p
        if c % 2 == 1:
            return F(x // p, p) + c
        else:
            return F(x // p, p) - c

results = []

for element in elements:
    if F(element, 3) == 0:
        results.append(element)

print(max(results))