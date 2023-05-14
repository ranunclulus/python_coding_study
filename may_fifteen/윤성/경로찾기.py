from collections import deque

N = int(input())  # 정점의 개수
graph = [list(map(int, input().split())) for _ in range(N)]  # 그래프의 인접행렬

def bfs(start):
    visited = [0 for _ in range(N)]  # 출발 위치에서 경로 존재 유무 및 방문 유무
    
    # 방문할 위치들 큐에 저장
    queue = deque()
    for i in range(N):
        if graph[start][i] == 1:
            queue.append(i)

    while queue:
        next = queue.popleft()  # 다음 방문 위치
        # 방문한 곳이라면 통과
        if visited[next] == 1:
            continue
        visited[next] = 1  # 방문 처리

        # 이동한 위치에서 방문할 수 있는 위치 추가
        for i in range(N):
            if graph[next][i] == 1 and visited[i] == 0:
                queue.append(i)

    return visited  # 연결된 경로 반환

# 하나의 출발 위치씩 확인하며 연결된 경로 결과 반환
for start in range(N):
    route = bfs(start)
    print(*route)