n = int(input())
f = False
for i in range(n):
    if int(input()) < 50:
        f = True
if f == True: print('No')
else: print("Yes")