n = int(input())
a = [int(x) for x in input().split()]
a = set(a)
a = list(a)
a.sort()
for i in a: print(i,end=' ')