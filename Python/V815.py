n = int(input())
a = []
for i in range(n): a.append(input().split())
a.sort(key=lambda x: int(x[1]), reverse=True)
for i in range(n): print(f"{i+1} {a[i][1]} {a[i][0]}")