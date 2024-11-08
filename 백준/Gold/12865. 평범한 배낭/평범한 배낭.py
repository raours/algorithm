N, K = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]


for i in range(N):
    for j in range(1,K+1):
        weight = bag[i][0] #넣을까 말까 체크할 물건 무게
        value = bag[i][1] #가치

        if weight >j: #넣어야할 가방 무게가 지금 기준 배낭 무게보다 크면
            dp[i][j] = dp[i-1][j] #못 넣음 -> 전에 턴 가방이랑 최대값 같음
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value) # 안넣었을때, 넣었을때

print(dp[N-1][K])