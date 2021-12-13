x, y = map(int,input().split())
a = [x,y]
a.sort()
for i in range(1,a[1]+1):
    if x%i==0 and y%i==0:
        ans = i
print(ans)
