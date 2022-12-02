m = -1
c = 0
while True:
    inp = input()
    if inp == "done":m=max(m,c);break
    elif inp == "": m=max(m,c);c = 0
    else: c+= int(inp)
print(m)
