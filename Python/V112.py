x, y = map(int,input().split())#
x = y - x
l = [10,5,2,1]
ll = ['$10','$5','$2','$1']
for i in range(4):
    t = int(x/l[i])
    x -= l[i]*t
    print(f"{ll[i]} coins: {t}")