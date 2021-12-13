x, y = map(int,input().split())
if x >= 170:
    if y>=60:
        print('Qualified')
    else:
        print('Not heavy enough')
else:
    if y>=60:
        print('Not tall enough')
    else:
        print('Not tall and heavy enough')