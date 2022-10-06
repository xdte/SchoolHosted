a = list(input())
flag = False
for i in a:
    if (ord(i) < 97 or ord(i) > 122) and i != '_':
        try:
            x = int(i)
        except ValueError or i == '_':
            flag = True
if (ord(a[0]) < 97 or ord(a[0]) > 122) or (len(a) < 6 or len(a) > 20) : flag = True 
print("Yes") if flag == False else print("No")