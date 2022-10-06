s = input()
a = list(s)
for i in range(len(a)+1):
    for j in a:
        print(j,end='')
    a.append(a[0])
    a.pop(0)
    print()