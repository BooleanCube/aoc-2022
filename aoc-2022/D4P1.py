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
    if x-y==set() or y-x==set(): ans += 1
print(ans)
