# x ≡ 32134 (mod 1584891)
# x ≡ 193127 (mod 3438478)

# x = a mod p
# x = b mod q

# kp + lq = 1
# lq = 1 mod p
# kp = 1 mod q
# x = alq + bkp

# kp + lq = 1
# p = tq + r
# k(tq + r) + lq = 1
# (kt + l)q + kr = 1
# k' = kt + l
# l' = k
# k = l'
# l = k' - tl' (t = p//q)

def ext_gcd(p, q):
    if q == 0:
        return 1, 0
    else:
        k, l = ext_gcd(q, p % q)
        return l, k - (p // q) * l


a = 32134
b = 193127
p = 1584891
q = 3438478
k, l = ext_gcd(p, q)

x = (a * l * q + b * k * p) % (p * q)
print(x)
