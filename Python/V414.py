n = int(input())
a = input().split()
for i in range(n): a[i] = int(a[i])
t = 0
flag = False
for i in range(n-1):
    t = a[i]
    if a[i+1] < t:
        flag = True
if flag == False: print("Yes")
else: print("No")
