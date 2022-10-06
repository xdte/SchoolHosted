n, m, x = map(int,input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
for i in range(n):
    for j in range(m):
        if a[i]+b[j]==x:
            print(a[i], b[j])