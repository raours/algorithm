'''
2025.9.16
'''
import sys
input=sys.stdin.readline


N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]

cnt = [0] * (d + 1)   # 각 초밥 번호의 현재 개수
distinct = 0 #서로 다른 초밥 가짓수

#첫 k개 초기화
for i in range(k):
    num = belt[i]
    if cnt[num] == 0:
        distinct += 1
    cnt[num] += 1

ans = distinct + (1 if cnt[c] == 0 else 0) #쿠폰에 써있는 초밥 추가
for i in range(1, N): #1~N-1까지 슬라이딩 윈도우

    #left에서 빠지는 부분
    left = belt[i-1]
    cnt[left] -= 1
    if cnt[left] == 0: #left 번째 종류 사라지면,
        distinct -= 1

    #right에 새로 들어오는 초밥
    right = belt[(i+k-1)%N] #원형
    if cnt[right] == 0:
        distinct += 1 #가짓수 +1
    cnt[right] += 1

    #ans 갱신
    cur = distinct+(1 if cnt[c] == 0 else 0) #distinct얘는 계속 유지
    ans = max(ans, cur)
print(ans)