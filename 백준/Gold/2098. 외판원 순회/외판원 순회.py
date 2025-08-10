'''
2025.8.10
백준 : 외판원 순회
'''
import sys

input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

# 그 지점부터 끝 지점까지 가는 값을 dp 테이블에 저장해놓고 쓰자
dp = [[None for _ in range(1<<n)] for _ in range(n)]
#dp[0][3] : 0번째 노드에서 1,2번째 노드는 방문한 상태이며,
# 이때 다른 노드까지 방문하는 최소 값을 미리 계산해놓은 dp값

#점화식: dp[current][visit] = min(dp[current][visit], dp[next][visit | (1<<next)]+lst[current][next]
# current 노드, 방문노드 상태가 visit 인 것 = min(현재값, 다음 노드&다음노드방문처리까지한 visit의 dp값 + current노드에서 next노드까지의 거리)


def dfs(current, visit):
    # 모든 노드를 다 거쳤으면,
    if visit == (1<<n) -1:
        if lst[current][0] != 0: #0번 으로 돌아갈 수 있는 경로가 있다면!
            return lst[current][0] #그 노드에서 0번으로 가는 거리가 dp값이 됨
        else: #돌아갈 수 있는 경로가 없다면 out!
            return 1e9 #그 dp값은 갈 수 없는 값이라고 써줘야함


    #방문한 노드, visit이면 바로 dp값 리턴
    if dp[current][visit] != None:
        return dp[current][visit]

    min_value = 1e9 #지금 dp값에 none이 들어가있는 곳이 있으므로, 최솟값 비교를 할 수가 없음
    for i in range(1, n): #0번 노드로 start했으므로,
        #방문하지 않은 노드에 대해, 경로가 존재한다면,
        if (visit & (1<<i)) == 0 and lst[current][i] != 0:
            min_value = min(min_value, dfs(i, visit|(1<<i)) + lst[current][i])
    dp[current][visit] = min_value #모든 노드에 대해 계산을 마친 최종 dp값 저장
    return min_value


print(dfs(0, 1))


