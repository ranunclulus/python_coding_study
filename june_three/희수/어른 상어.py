# 백준 19237
from collections import deque

# 방향 설정 (1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# n: 격자 크기 / m: 상어 개수 / k: 냄새 지속 시간 / time: 총 시간
n, m, k = map(int, input().split())
time = 0

# 상어가 위치해 있는 2차원 배열
smell = []
for i in range(n):
    smell.append(list(map(int, input().split())))

# 상어의 향기 지속 시간을 저장하는 배열
time = [[0 for j in range(n)] for i in range(n)]

# 상어의 위치 찾기
sharks = []
for num in range(1, m + 1):
    for i in range(n):
        for j in range(n):
            if smell[i][j] == num:
                sharks.append([i, j])

# 상어의 방향 입력받기
direction = list(map(int, input().split()))
for i in range(m):
    sharks[i].append(direction[i])
direction = []

# 상어가 있는 곳 향기 바꾸기
for i in range(m):
    x, y = sharks[i][0], sharks[i][1]
    time[x][y] = k

# 상어의 방향 우선 순위 입력받음
for shark in range(m):
    shark_dir = []
    for _ in range(4):
        shark_dir.append(list(map(int, input().split())))
    direction.append(shark_dir)

# 상어의 흔적들을 저장하는 데이터
smell_print = [deque() for _ in range(m)]
# 흔적 데이터에 초기 상어 위치 넣어 주기
for i in range(m):
    smell_print[i].append([sharks[i][0], sharks[i][1]])

# 상어의 방향을 결정하는 함수
# 1. 어떤 상어의 냄새도 없어야 한다
# 2. 보드 안이어야 한다
# 3. 우선 순위에 따라 움직인다
def move_sharks(sharks, time, smell, smell_print):
    for i in range(m):
        # 상어 한 마리의 x 좌표, y 좌표, 방향
        x, y, shark_dir = sharks[i]
        # 상어의 방향에 따른 우선 순위 불러오기
        priority = direction[i][shark_dir - 1]
        more_to_search = True
        # 우선 순위에 따른 방향 이동 검색
        for j in priority:
            nx, ny = x + dx[j -1], y + dy[j - 1]
            if 0 <= nx < n and 0 <= ny < n and more_to_search: # 보드 범위 안이라면
                # 상어를 먹을 수 있을 때
                if smell[nx][ny] == 4:
                    print("먹을 때가 왔다")
                    print(x, y, smell[x][y])
                    print(nx, ny, smell[nx][ny])
                    print(priority)
                    continue
                # 이동이 가능할 때
                elif smell[nx][ny] == 0:
                    smell[nx][ny] = i + 1 # 상어의 번호 표시
                    smell_print[i].append([nx, ny])  # 새로운 위치 넣어 주기
                    time[nx][ny] = 5 # 향기 표시
                    sharks[i] = [nx, ny, j] # 상어의 현재 위치 다시 표기
                    # 큐가 4까지 다 차 있으면 하나 삭제해 줌
                    if (len(smell_print[i]) == 4):
                        smell_print[i].pop()
                    # 발자국을 돌면서 향기를 하나씩 감소시킴
                    for footprint in smell_print[i]:
                        ix, iy = footprint
                        time[ix][iy] = time[ix][iy] - 1
                    more_to_search = False
                # else 인 경우는 이동 불가능하기 때문에 아무 행위도 하지 않음
                else:
                    continue
            else: # 보드 범위 밖이라면
                continue

# 확인용 프린트
def print_all(smell, sharks, time, direction, smell_print):
    print("smell")
    for i in smell:
        print(i)
    print("------")

    print("sharks")
    print(sharks)
    print("------")

    print("time")
    for i in time:
        print(i)
    print("------")

    print("direction")
    for i in range(m):
        print(i, "번쨰 상어")
        for j in range(4):
            print(direction[i][j])
        print()
    print("------")

    print("smell_print")
    for smell in smell_print:
        print(smell)
    print("------")

print_all(smell, sharks, time, direction, smell_print)

move_sharks(sharks, time, smell, smell_print)

print_all(smell, sharks, time, direction, smell_print)

move_sharks(sharks, time, smell, smell_print)

print_all(smell, sharks, time, direction, smell_print)