import re
l = [[0]]
for i in range(9):
    l.append(list(input()))
n = int(input())
for i in range(n):
    x,a,b = map(int, re.findall(r"\d+", input()))
    for j in range(x):
        if len(l[a]) == 0: break
        l[b].append(l[a][-1])
        l[a].pop(-1)
print("".join(c[-1] for c in l[1:]))
