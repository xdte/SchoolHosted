l = []
while True:
    x = int(input())
    if x == -1:
        break
    l.append(x)
sum = l[0]
for i in range(1,len(l)):
    sum = sum*l[i]
print(sum)