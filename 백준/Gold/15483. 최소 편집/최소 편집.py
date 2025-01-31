

#input = sys.stdin.readline 얘는 개행문자를 같이 가져옴

bef = input()
aft = input()
n = len(bef)
m = len(aft)

#dp초기 설정
dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][0] = i
for j in range(1,m+1):
    dp[0][j] = j

for i in range(1,n+1):
    for j in range(1, m+1):
        if bef[i-1] == aft[j-1]: #행, 열 문자가 같으면 왼쪽 위 숫자 그대로
            dp[i][j] = dp[i-1][j-1]
        else: #행, 열 문자 다르면 min 삽입(왼쪽), 삭제(위), 교체(왼쪽 위) 중 하나 +1
            temp = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
            dp[i][j] = temp+1

print(dp[n][m])