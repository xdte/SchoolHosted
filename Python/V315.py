n = int(input())
m = 101
for i in range(n):
    x = int(input())
    if x < m:
        m = x
print(m)