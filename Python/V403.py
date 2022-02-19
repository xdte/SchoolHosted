n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
b = input().split()
for i in range(n):
    b[i] = int(b[i])
for i in range(n):
    a[i] += b[i]
for i in a:
    print(i,end=" ")