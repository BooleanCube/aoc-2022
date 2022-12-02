score = {"X":1, "Y":2, "Z":3}
win = ['A Y', 'B Z', 'C X']
draw = ['A X', 'B Y', 'C Z']
s = 0
while 1:
    inp = input()
    if inp == "done":break
    s += 6 if inp in win else 3 if inp in draw else 0
    s += score[inp.split()[1]]
print(s)
