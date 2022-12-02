score = {"X":1, "Y":2, "Z":3}
value = {"A":1, "B":2, "C":3}
opts = "XYZ"
s = 0
while 1:
    inp = input()
    if inp == "done":break
    l=inp.split()
    h=l[0]
    d=l[1]
    i = value[h]-1
    s += 6 if d=="Z" else 3 if d=="Y" else 0
    s += score[opts[(i+1)%3]] if d=="Z" else score[opts[i]] if d=="Y" else score[opts[i-1]] 
print(s)
