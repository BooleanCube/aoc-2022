p = 0
a = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
while 1:
    r = input()
    if r == "done": break
    r2 = input()
    r3 = input()
    d = set(r).intersection(set(r2)).intersection(set(r3))
    for i in d: p += a.index(i)
print(p)
