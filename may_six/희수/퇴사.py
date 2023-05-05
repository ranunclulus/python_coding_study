import sys
input = sys.stdin.readline
n = int(input())

dp = [0] * 20
tplist = [[0, 0]]
for _ in range(n):
    t, p = map(int, input().split())
    tplist.append([t, p])

for i in range(1, n + 1):
    x = tplist[i][0] - 1
    dp[i] = max(dp[i - 1], dp[i])
    dp[i + x] = max(dp[i - 1] + tplist[i][1], dp[i + x])

print(dp[n])