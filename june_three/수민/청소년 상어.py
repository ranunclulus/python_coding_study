
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1 1]

graph = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        graph[i][j] = [data[j * 2], data[j * 2 + 1] - 1 ]

result = graph[0][0][0]
direction = graph[0][0][1]
graph[0][0][0] = -1

def find_fish_index(value):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == value:
                return i, j
    return -1

def turn_left(dir):
    return (dir+1) % 8

def fish_move(x, y):
    for i in range(8):
        if i == 0:
            dir = graph[x][y][1]
        if i > 0:
            dir = turn_left(dir)
        nx = x + dx[dir]
        ny = y + dy[dir]
        if graph[nx][ny] >= 1 and graph[nx][ny] <= 16:
            graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
            return
    
def all_fish_move():
    for i in range(1, 17):
        if find_fish_index(i) != -1:
            i, j = find_fish_index(i)
            fish_move(i, j)
