'''
2025.8.13
백준 : 크로아티아 알파벳
'''
import sys

st = input()

alpabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
ans = 0
i = 0
while i<len(st):
    if st[i:i+2] in alpabet: #  크알 있으면,
        i += 2
    elif st[i:i+3] == 'dz=': #  크알 있으면,
        i = i+3
    else:
        i += 1
    ans += 1
print(ans)