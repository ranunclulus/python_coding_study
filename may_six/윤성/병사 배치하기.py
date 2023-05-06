N = int(input())  # 병사의 수
power = list(map(int, input().split()))  # 병사의 전투력

dp = [1 for _ in range(N)]  # 인덱스까지 내림차순 최대 병사의 수
# 두번째 병사부터 한 명씩 탐색
for now in range(1, N):
    for prev in range(now):
        # 현재 위치의 병사보다 앞쪽 병사 중 전투력이 더 큰 병사인 경우에만 앞에 위치 가능
        if power[prev] > power[now]:
            dp[now] = max(dp[prev] + 1, dp[now])

print(N - max(dp))  # 결과 출력