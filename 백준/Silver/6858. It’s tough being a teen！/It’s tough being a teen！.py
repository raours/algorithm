'''
2025.9.21
'''
import sys
import heapq
input=sys.stdin.readline

con = [0]*8
lst = [[] for _ in range(8)]

#처음 조건들
ini = [(1,7),(1,4),(2,1),(3,4),(3,5)]

while True:
    x = int(input().strip())
    y = int(input().strip())

    if (x,y) == (0,0):
        break
    ini.append((x,y))

#조건 반영
for x,y in ini:
    con[y] += 1 #진입차수 +1
    lst[x].append(y)

#위상 정렬
hq = []
ans = []
for i in range(1,8): #진입 차수 0인 곳에서 start
    if con[i] == 0:
        heapq.heappush(hq,i)
while hq:
    start = heapq.heappop(hq)
    ans.append(start)

    #연결되어 있는 간선 끊기
    for next in lst[start]:
        con[next] -= 1
        if con[next] == 0: #진입차수 0됐으면, q에 넣기
            heapq.heappush(hq,next)

if len(ans) == 7: #모든 노드 다 거쳤으면, 위상정렬 가능!
    print(*ans)
else:
    print('Cannot complete these tasks. Going to bed.')

