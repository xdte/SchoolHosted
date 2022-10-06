n, x = map(int,input().split())
a = [int(x) for x in input().split()]
for i in range(n):
    for j in range(i+1,n):
        if a[i]+a[j]==x:
            print(a[i], a[j])