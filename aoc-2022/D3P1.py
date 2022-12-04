p = 0
a = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
while 1:
    r = input()
    if r == "done": break
    fc = r[:len(r)//2]
    sc = r[len(r)//2:]
    d = set(fc).intersection(set(sc))
    for i in d: p += a.index(i)
print(p)
