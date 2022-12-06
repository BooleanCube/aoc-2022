n = 4
s = input()
print([i+n for i in range(len(s)-n+1) if len(set(s[i:i+n]))==n][0])
