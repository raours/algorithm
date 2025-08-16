'''
2025.8.16
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = [num for num in range(1,n+1)]
ans = []
idx = 0
while len(lst)>0:
    idx += (k-1)
    if idx >= len(lst): #리스트 범위 넘어가면,
        idx = idx % len(lst)
    ans.append(str(lst.pop(idx))) #그 인덱스 값 pop해서 ans에 붙여주기

#join 이용해서 문자열 간단하게 출력    
print('<'+', '.join(ans)+'>')

