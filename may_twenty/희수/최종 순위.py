from collections import deque
import copy

# 테스트 케이스 개수 입력받기
test_case = int(input())

# 노드의 개수 입력받기
v = int(input())

# 모든 노드에 대한 진입차수 0으로 초기화
indegree = [0] * (v + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력받기
last_rank = list(map(int, input().split()))
last_rank.reverse()
for i in range(v - 1):
    indegree[last_rank[i]] += 1
    graph[last_rank[i]].append(last_rank[i + 1])

print(graph)
print(indegree)

m = int(input())

# 간선 업데이트
for i in range(m):


# 위상 정렬 함수
def topology_sort():
    # 알고리즘 수행 결과를 담을 리스트
    result = copy.deepcopy(time)
    q = deque()

    # 처음 시작할 때 진입차수가 0인 노드 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v + 1):
        print(result[i])

topology_sort()
