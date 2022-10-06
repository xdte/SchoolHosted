s = input()
t = input()
cur = 0
cnt = 0
for i in range(len(s)-len(t)+1):
    if s[i:i+len(t)] == t:
        cnt += 1
print(cnt)