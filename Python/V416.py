a = [[0]*100 for i in range(100)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    a[y-1][x-1] = 1
q = int(input())
for i in range(q):
    flag = False
    x1, y1, x2, y2, = map(int, input().split())
    for j in range(y1-1,y2):
        for k in range(x1-1, x2):
            if a[j][k] == True:
                flag = True
                break
    print('Yes') if flag == True else print("No")