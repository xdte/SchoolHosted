m, n = map(int,input())
a = []
for i in range(m):
    x = input().split()
    a.append(x)
q = int(input())
for i in range(q):
    x, y = map(int,input())
    print(a[x][y])