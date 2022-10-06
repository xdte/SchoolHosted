s = input().lower()
a = list(s)
cnt = 0
for i in a:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i =='u' or i == 'y':
        cnt+=1#
print(cnt)