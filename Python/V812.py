n = int(input())
a = []
for i in range(n):
    a.append(input())
al = [[] for i in range(6)]
for i in a:
    al[int(i[0])-1].append(i)
for i in range(6):
    al[i].sort()
for i in range(5,-1,-1):
    for j in al[i]:
        print(j)