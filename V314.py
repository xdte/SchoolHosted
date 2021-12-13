a = []
sum = 0
while True:
    x = int(input())
    if x == -1:
        break
    a.append(x)
for i in a:
    sum+=i
print(f"{sum/len(a):.6f}")