from collections import deque

INF = 1e9

n= int(input())
graph = []
global shark 
shark = 2 # 상어의 크기
global now_x, now_y # 상어의 위치
now_x, now_y = 0, 0 

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상어의 시작위치에 대해서 물고기까지 거리 update하는 함수
def bfs():
    distance = [[-1] * n for _ in range(n)]
    q = deque([(now_x, now_y)])
    distance[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵 밖에 벗어나는 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 물고기 크기가 상어의 크기보다 큰 경우
            if graph[nx][ny] > shark:
                continue
            if distance[nx][ny] != -1:
                continue
            if nx == now_x and ny == now_y:
                continue
            distance[nx][ny] = distance[x][y] + 1
            q.append((nx, ny))
    return distance

# 상어가 먹을 수 있는 첫번째 물고기 크기와 좌표를 return 하는 함수
def find_fish(dist):
    min_value = INF
    # 값이 같은 가장 위 그 다음 가장 왼쪽 => x가 작은 값 그 다음 y가 작은 값
    for i in range(n):
        for j in range(n):
            # 물고기가 없는 경우와 물고기 있는데 상어 크기 보다 작지 않는 경우
            if graph[i][j] >= shark or graph[i][j] == 0:
                continue
            if min_value >= dist[i][j]:
                x, y = i, j
                min_value = dist[i][j]
    if min_value == INF:
        return -1
    return x, y, min_value


count = 0
result = 0
while True:
    dist = bfs()
    if find_fish(dist) == -1:
        break
    else:
        x, y, short = find_fish(dist)
        now_x, now_y = x, y
        result += short
        graph[x][y] = 0
        count += 1
        if count >= shark:
            shark += 1
            count = 0
print(result)