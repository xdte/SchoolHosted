n = int(input())
x = input().split()
q = int(input())
for i in range(q):
    a, b = map(int,input().split())
    tmp = x[a]
    x[a] = x[b]
    x[b] = tmp
for i in x:
    print(i,end=" ")    