import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]

house.sort()
# 공유기를 어디에 설치할지가 아니라
# 최대거리를 이진 탐색으로 찾아내는 것임
start = house[0]-house[1] # 최단거리
end = house[-1] - house[0] #최대거리
answer = 0
while start<= end:
    mid = (start+end)//2

    first = house[0] #첫번째 집에 공유기 설치
    cnt = 1 #공유기 갯수
    
    #공유기 설치
    for i in range(1,N):
        if (house[i] - first) >= mid:
            cnt +=1
            first = house[i]

    #공유기 갯수 확인
    if cnt >= C:
        start = mid+1
        answer = mid
    else:
        end = mid-1

print(answer)
    
        