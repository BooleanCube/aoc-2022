z = 5
visible = set()
side = [[0]*z for i in range(z)]
for i in range(z):
    line = list(map(int, list(input())))
    for j in range(z): side[j][i] = line[j]
    pn = -1
    pi = -1
    for j in range(z):
        if line[j] > pn:
            pn = line[j]
            visible.add((i,j))
        if line[z-j-1] > pi:
            pi = line[z-j-1]
            visible.add((i,j))
for i in range(z):
    pn = -1
    pi = -1
    line = side[i]
    print(line)
    for j in range(z):
        if line[j] > pn:
            pn = line[j]
            visible.add((j,i))
        if line[z-j-1] > pi:
            pi = line[z-j-1]
            visible.add((j,i))
for t in visible:
    print(t, side[t[1]][t[0]])
print(len(visible))

