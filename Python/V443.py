n = int(input())
a = [int(x) for x in input().split()]
o = int(input())
for i in range(o):
    op = [int(x) for x in input().split()]
    if op[0] == 1:
        a.insert(op[1],op[2])
    else:
        a.pop(op[1])
print(len(a))
for i in a: print(i,end=' ')