n = int(input())
a = [0]*1444
for i in range(n):
    start, end = input().split()
    start1, start2 = map(int, start.split(":"))
    end1, end2 = map(int, end.split(":"))
    start = start1*60 + start2
    end = end1*60 + end2
    a[start] += 1
    a[end] -= 1
cur = 0
mx = 0
for i in range(len(a)):
    cur += a[i]
    if cur > mx:
        mx = cur
print(mx)