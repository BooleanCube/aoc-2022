import re
lines = []
while 1:
    cinp = input()
    if cinp!="done": lines.append(cinp)
    else:break
ans = 0
for line in lines:
    a,b,c,d = map(int, re.findall(r"\d+", line))
    x = set(range(a,b+1))
    y = set(range(c,d+1))
    if len(x.intersection(y)) > 0: ans += 1
print(ans)
