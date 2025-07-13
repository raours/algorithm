'''
2025.7.13
백준 : 단어수학
'''
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
dic = {}
for i in range(n):
    st = list(map(str,input().strip()))
    for j in range(len(st)):
        if st[j] not in dic:
            dic[st[j]] = 10**(len(st)-j-1)
        else:
            dic[st[j]] += 10**(len(st)-j-1)


dic2 = sorted(dic.items(), key = lambda x: x[1], reverse= True)
ans = 0
for idx in range(len(dic2)):
    ans += dic2[idx][1]*(9-idx)
    
print(ans)