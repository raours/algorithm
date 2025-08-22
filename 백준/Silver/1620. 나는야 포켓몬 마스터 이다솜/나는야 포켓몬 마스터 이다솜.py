'''
2025.8.22
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
for i in range(1,n+1):
    dic[i] = input().strip()
lst = [input().strip() for _ in range(m)]
reverse_dic = dict(map(reversed, dic.items())) #시간 초과 나지 않게 먼저 reverse 된 딕셔너리 생성해놓기!

for i in range(m):
    if lst[i].isalpha(): #포켓몬 이름
        print(reverse_dic[lst[i]] )
    
    else: #번호
         print(dic[int(lst[i])])
