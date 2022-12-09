filesize = {}
line = input()
cf = []
while line!="done":
    latest = None
    if line[0] == "$":
        if line[2:] == "cd ..": cf.pop(-1)
        elif line.split()[1] == "cd": cf.append(line.split()[2])
        elif line[2:] == "ls":
            for f in cf: filesize[f] = 0 if f not in filesize else filesize[f]
            while True:
                l = input()
                latest = l
                if l=="done": break
                if l[0] == "$": break
                if l[:3] == "dir": continue
                fs = int(l.split()[0])
                for f in cf: filesize[f] += fs
    if latest == "done": break
    if latest != None: line = latest
    else: line = input()
print(sum(filesize[f] for f in filesize if filesize[f]<=100000))
