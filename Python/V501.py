a = input().split()
x = a[0]
y = a[1]
a.sort()
if x ==y:
    print("Same")
elif a[0] == x:
    print("Smaller")
else:
    print("Larger")