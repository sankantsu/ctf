def decode(s, off):
    res = ""
    for c in s:
        c2 = c
        if c.isalpha():
            c2 = chr(ord(c) + off)
        res += c2
    return res


crpt = "fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}"
print(crpt)

offs = [3, -3]
ans = [decode(crpt, off) for off in offs]
for s in ans:
    print(s)
