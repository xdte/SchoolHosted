x, y = map(int,input().split())
if x > 2 and y > 2:
  for i in range(y):
    print('*',end='')
  print()
  for i in range(x-2):
    print('*',end='')
    for o in range(y-2):
      print(' ',end='')
    print('*')
  for i in range(y):
    print('*',end='')
else:
  for i in range(x):
    for j in range(y):
      print("*",end='')
    print()
