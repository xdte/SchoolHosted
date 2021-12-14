n = int(input())
t = n/2.54
f = t//12
t-=f*12
if round(t) == 12:
    t = 0
    f+=1
print(f"{int(f)} {round(t)}")