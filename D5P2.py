import re
l = [[0]]
for i in range(9):
    l.append(list(input()))
n = int(input())
for i in range(n):
    x,a,b = map(int, re.findall(r"\d+", input()))
    l[b] += l[a][-x:-1] + [l[a][-1]]
    l[a] = l[a][:-x]
print("".join(c[-1] for c in l[1:]))
