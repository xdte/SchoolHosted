n = int(input())
f = False
for i in range(n):
    if int(input()) < 50:
        f = True
if f == True: print('Yes')
else: print("No")