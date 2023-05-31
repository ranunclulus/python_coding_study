import sys
from collections import deque

input = sys.stdin.readline
n = int(input()) # 보드 크기
board = []
for _ in range(n):
    board.append((list(map(int, input().split()))))

shark_x, shark_y, shark_size = 0, 0, 2

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 아기 상어의 위치 찾기
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            shark_x, shark_y = i, j

def find_fish(x, y, shark_size):
    fishes = []
    q = deque()
    visited = [[0] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if board[nx][ny] <= shark_size: # 이동이 가능할 때
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    if board[nx][ny] < shark_size and board[nx][ny] != 0: # 먹을 수 있을 때
                        fishes.append([nx, ny, distance[nx][ny]])
    fishes.sort(key = lambda x: (x[2], x[0], x[1]))
    return fishes

eat, result = 0, 0
while 1:
    fishes = find_fish(shark_x, shark_y, shark_size)

    if len(fishes) == 0: # 먹을 수 있는 물고기가 없으면 종료
        print(result)
        break
    else:
        shark_x, shark_y, dis = fishes[0]
        eat += 1
        board[shark_x][shark_y] = 0
        result += dis
        if (eat == shark_size):
            shark_size += 1
            eat = 0
