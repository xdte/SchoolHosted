a = input().lower()
store = [0]*26
for i in a:
    if ord(i)>=97 and ord(i) <= 122: store[ord(i)-97] += 1
for i in range(26): 
    if store[i] != 0: print(f"{chr(i+97)}: {store[i]}")