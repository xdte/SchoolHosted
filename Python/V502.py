a = list(input())
for i in a:
    if ord(i) > 96 and ord(i) < 123:
        print(chr(ord(i)-32),end="")
    else:
        print(i,end="")