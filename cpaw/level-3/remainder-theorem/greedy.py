a = 32134
b = 193127
p = 1584891
q = 3438478


x = b
for i in range(p):
    if x % p == a:
        break
    x += q
print(x)
