score = {"X":1, "Y":2, "Z":3}
value = {"A":1, "B":2, "C":3}
su = 0
while 1:
    inp = input()
    if inp == "done":break
    l = inp.split()
    c = 0
    s = value[l[0]]
    e = score[l[1]]
    c += e
    if e>s or s-e==2: c += 6
    elif s==e: c += 3
    su += c
print(su)
