import copy

fishes = []
# 물고기 입력받기
for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        fish.append(data[2 * j:2 * j + 2]) # [물고기 크기, 물고기 방향]으로 입력받기
    fishes.append(fish)

# 몇 번째 크기의 물고기가 먹혔나
dead_fish = [0] * 17 # 몇 번째 크기의 물고기가 먹혔나
dead_fish[fishes[0][0][0]] = 1
# 결과 저장
result = fishes[0][0][0]
# (0, 0)에 상어 위치시키기
shark_x, shark_y = 0, 0

print(dead_fish)

# 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미
     # 0  1   2  3  4  5  6  7
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 가장 작은 물고기가 있는 좌표를 받았을 경우 방향을 이동하는 함수
def swap_fish(min_x, min_y):
    dir = fishes[min_x][min_y][1] - 1
    for i in range(8):
        dir = (dir + i) % 8
        nx, ny = min_x + dx[dir], min_y + dy[dir]
        if 0 <= nx < 4 and 0 <= ny < 4 and fishes[nx][ny][0] != 0: # 보드 안에 있고 상어가 있는 곳이 아니라면
            fishes[min_x][min_y][1] = dir + 1 # 방향 다시 설정
            fishes[nx][ny], fishes[min_x][min_y] = fishes[min_x][min_y], fishes[nx][ny] # 물고기끼리 이동
            break

# 물고기 전체를 이동하는 함수
def move_fish():
    val = 1
    while val <= 16:
        if dead_fish[val] == 0: # 먹은 적 없는 물고기 크기일 때
            for i in range(4):
                for j in range(4):
                    if fishes[i][j][0] == val:
                        swap_fish(i, j)
                        val += 1
                        break
        else: # 이미 먹은 크기일 때 -> 존재하지 않기 때문에 물고기 이동 불필요
            val += 1

# 상어가 먹을 수 있는 물고기 좌표 찾기
def can_eat(shark_x, shark_y):
    possible = []
    dir = fishes[shark_x][shark_y][1] - 1
    nx, ny = shark_x, shark_y
    for i in range(4):
        nx, ny = nx + dx[dir], ny + dy[dir]
        if 0 <= nx < 4 and 0 <= ny < 4 and fishes[nx][ny][0] != 0:
            possible.append([nx, ny])
    return possible


def dfs(shark_x, shark_y, eat):
    global result
    dead_fish[fishes[shark_x][shark_y][0]] = 1
    eat += fishes[shark_x][shark_y][0]
    fishes[shark_x][shark_y][0] = 0
    move_fish()
    possible = can_eat(shark_x, shark_y)
    if len(possible) == 0:
        result = max(result, eat)
        return
    else:
        for nx, ny in possible:
            dfs(nx, ny, eat)

dfs(shark_x, shark_y, 0)
print(result)



