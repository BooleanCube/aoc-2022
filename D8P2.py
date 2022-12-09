data = [input() for _ in range(99)]
forest = [[int(x) for x in row] for row in data]
side = list(zip(*forest))
score = 0
def length(tree, view):
    l = 0
    for v in view:
        l += 1
        if v >= tree:
            break
    return l
for i in range(len(forest[0])):
    for j in range(len(forest)):
        tree = forest[i][j]
        a = length(tree, forest[i][:j][::-1])
        b = length(tree, forest[i][j+1:])
        c = length(tree, side[j][:i][::-1])
        d = length(tree, side[j][i+1:])
        score = max(score, a*b*c*d)
print(score)
