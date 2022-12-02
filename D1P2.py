m=[]
c = 0
while True:
    inp = input()
    if inp == "done":m.append(c);break
    elif inp == "": m.append(c);c = 0
    else: c+= int(inp)
s = max(m)
m.remove(s)
a = max(m)
s += a
m.remove(a)
s += max(m)
print(s)
