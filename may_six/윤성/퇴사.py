t(max(dp))
N = int(input())  # 근무 기간

T, P = [0], [0]  # 상담 소요 시간, 상담료
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 2)
for day in range(1, N + 1):
    # 어제까지의 상담료가 더 비싼 경우
    if dp[day - 1] > dp[day]:
        dp[day] = dp[day - 1]
    # 퇴사 전에 상담이 가능한 경우
    if day + T[day] <= N + 1:
        dp[day + T[day]] = max(P[day] + dp[day], dp[day + T[day]])

print(max(dp))  # 결과 출력