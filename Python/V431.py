n = int(input())
a = input().split()
b = [0] *11
for i in a:
    b[int(i)] += 1
for i in range(1,11):
    print(f"{i}: {b[i]}")