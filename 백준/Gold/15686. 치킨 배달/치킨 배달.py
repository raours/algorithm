import sys
from itertools import combinations, permutations
#sys.stdin = open("input2.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
D = 1000000 # 도시의 치킨거리
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i,j)) # 집 좌표 저장
        elif city[i][j] ==2:
            chicken.append((i,j)) #치킨집 좌표 저장

combi = list(combinations(chicken, M)) #치킨 집에서 M개 뽑는 조합

for i in range(len(combi)): # 치킨 집 조합을 하나씩 꺼내서
    d = [200]*len(home) #각 집의 치킨거리 저장소
    for j in range(len(home)): #집 하나씩
        for k in range(M): #각 치킨집 마다
            chi_r, chi_c = combi[i][k]
            d[j] = min(d[j],abs(chi_r-home[j][0])+abs(chi_c-home[j][1])) #각 집의 치킨거리 구함
    D = min(D, sum(d))

print(D)



