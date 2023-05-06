N = int(input())  # 삼각형의 크기

# 삼각형 정보
triangle = []
for y in range(N):
    triangle.append(list(map(int, input().split())))

dp = []  # 삼각형 위치별 경로 합의 최대값 
for y in range(N):
    dp.append([0 for _ in range(y + 1)])

dx = [-1, 0]  # 가로 축 이동

# 최고층 초기값 저장 후 아래층으로 이동
dp[0][0] = triangle[0][0]
for y in range(1, N):
    # 현재 층 가로로 이동하며 dp 업데이트
    for x in range(y + 1):
        # 대각선 왼쪽과 대각선 오른쪽 확인
        for d in range(2):
            px, py = x + dx[d], y - 1  # 대각선 위치의 좌표
            # 삼각형 범위 밖인 경우 통과
            if not (0 <= px < y):
                continue
            dp[y][x] = max(dp[y][x], dp[py][px] + triangle[y][x])  # 경로 합의 최대값 업데이트

print(max(dp[-1]))  # 결과 출력