import heapq
import sys

input = sys.stdin.readline

N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수

# 버스 노선 정보 저장
graph = [[int(1e7) for x in range(N + 1)] for y in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, input().split())  # 출발 도시, 도착 도시, 버스 비용
    graph[start][end] = min(graph[start][end], cost)

# 출발 위치별 다른 도시로 가는데 필요한 최소 비용 출력
for start in range(1, N + 1):
    distance = [int(1e7) for _ in range(N + 1)]  # 현재 위치에서의 비용
    pq = []  # 방문할 위치 저장 (우선순위큐)

    # 출발지 추가
    heapq.heappush(pq, (start, 0))
    distance[start] = 0

    while pq:
        now, cost = heapq.heappop(pq)
        # 더 적은 비용으로 방문하는 경로로 방문할 수 있는 경우 통과
        if distance[now] < cost:
            continue
        # 현재 위치에서 방문할 수 있는 장소 추가
        for i in range(1, N + 1):
            # 버스 노선이 없는 경우 통과
            if graph[now][i] == int(1e7):
                continue
            # 현재 위치에서 가는 것이 더 큰 비용이 소모되는 경우 통과
            if distance[i] <= distance[now] + graph[now][i]:
                continue
            heapq.heappush(pq, (i, distance[now] + graph[now][i]))
            distance[i] = distance[now] + graph[now][i]

    # start에서 다른 도시로 가는데 필요한 최소 비용 출력
    for end in range(1, N + 1):
        print(distance[end] if distance[end] != int(1e7) else 0, end=' ')
    print()