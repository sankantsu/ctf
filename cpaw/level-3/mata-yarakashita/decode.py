# read input
lst = []
while True:
    try:
        s = input()
        b = int(s, 16)
        lst.append(b)
    except EOFError:
        break

# convert
lst = list(map(lambda x: x ^ 25, lst))

# make string and print
s = "".join(map(chr, lst))
print(s)
