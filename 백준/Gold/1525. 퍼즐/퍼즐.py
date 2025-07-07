'''
2025.7.6-7/7
백준 : 퍼즐
'''
from collections import deque
import sys

input = sys.stdin.readline

lst = ''
for i in range(3):
    temp = input().strip().replace(" ", "")
    for j in range(3):
        if temp[j] == '0':
            er,ec = i,j
    lst += temp

visit = {lst}
q = deque()
q.append((er,ec,0,lst))

dr = [0,-1,0,1]
dc = [1,0,-1,0]
answer = -1

flag = False
while q:
    r,c,d,chk = q.popleft()
    if chk == '123456780':
        print(d)
        flag = True
        break

    for i in range(4):
        nr, nc = r+dr[i],c+dc[i]
        if 0<=nr<3 and 0<=nc<3 : #바꿀 숫자가 범위내에 있고
            chk = list(chk) #문자열 내에서는 자리를 못 바꾸니까 리스트로 만들기
            chk[r*3+c],chk[nr*3+nc] = chk[nr*3+nc],chk[r*3+c] #자리 체인지
            tmp = ''.join(chk) #다시 문자열로!
            #바꿨을 때, 문자열로 만들어서 visited랑 비교하기!
            if tmp not in visit:
                #한번도 만들어진 적 없는 경우면!
                q.append((nr,nc,d+1,tmp))
                visit.add(tmp)
            chk[r*3+c],chk[nr*3+nc] = chk[nr*3+nc],chk[r*3+c] #다시 자리 체인지-> for문을 돌고 있으니까!
        

if flag == False:
    print(answer)