x = int(input())
for i in range(int(x/2)):
    for j in range(i):
        print(" ",end="")
    print("*",end="")
    for j in range(x-2-(2*i)):
        print(" ",end="")
    print("*")
if x%2==1:
    for i in range(int(x/2)):
        print(" ",end="")
    print("*")
for i in range(int(x/2)):
    for j in range(int(x/2)-1-i):
        print(" ",end="")
    print("*",end="")
    for j in range(2*i):
        print(" ",end="")
    if x%2==1:
        print(" ",end="")
    print("*")