a = list(input())
f = False
for i in a:
    if ord(i) < 97 or ord(i) > 122:
        f = True
if f == True:
    print("No")
else:
    print("Yes")