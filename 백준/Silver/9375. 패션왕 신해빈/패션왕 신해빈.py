'''
2025.8.23
'''
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dic = {}
    for _ in range(n):
        clothes, kinds = input().split()
        if kinds in dic: #같은 종류 이미 있으면,
            dic[kinds].append(clothes)
        else:
            dic[kinds] = [clothes]
    ans = 1
    for k,v in dic.items():
        ans *= (len(v)+1) # 각 종류에서 0개 or 그 요소 중 하나 뽑는 경우수
    print(ans-1) #모두 0인 경우는 빼주기
