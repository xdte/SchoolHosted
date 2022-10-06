s = input()
t = input()
mx = 0
for i in range(len(t)):
    for j in range(i, len(t)+1):
        tar = t[i:j]
        if s.find(tar) != -1:
            if abs(i-j) > mx:
                mx = abs(i-j)
print(mx)