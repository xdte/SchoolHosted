n = int(input())
m=[]
a = input().split()
b = [False] *10
for i in a:
    b[int(i)-1] = True
for i in range(10):
    if b[i] == False:
        m.append(i+1)
if len(m) == 0:
    print("No missing")
else:
    for i in m:
        print(f"{i} ",end="")