x, y = map(int,input().split())
for i in range(x):
  for o in range(y):
    print(f"{i+1} x {o+1} = {(i+1)*(o+1)}")
  print()