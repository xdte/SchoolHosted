n = int(input())
a = [0]*86405
for i in range(n):
    start, end = input().split()
    start1, start2, start3 = map(int, start.split(":"))
    end1, end2, end3 = map(int, end.split(":"))
    start = start1*3600 + start2*60 + start3
    end = end1*3600 + end2*60 + end3
    a[start] += 1
    a[end] -= 1
cur = 0
mx = 0
for i in range(len(a)):
    cur += a[i]
    if cur > mx:
        mx = cur
print(mx)