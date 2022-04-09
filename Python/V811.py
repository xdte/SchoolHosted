n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
a.sort(reverse=True)
for i in a:
    print(f"{i} ",end="")