n = int(input())
a = input().split()
x = input()
t = -1
for i in range(n):
    if a[i] == x:
        t = i
        break
if t == -1: print("Not found")
else: print(t)