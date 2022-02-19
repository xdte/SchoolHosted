n = int(input())
x = input().split()
for i in range(n):
    x[i] = int(x[i])
x.sort()
print(x[n-1])