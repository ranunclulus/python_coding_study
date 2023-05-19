import sys
from collections import deque

input = sys.stdin.readline

# 위상정렬
def topology_sort(graph, indegree):
    result = []  # 위상정렬 결과
    queue = deque()  # 다음 연결될 노드

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, len(graph)):
        if indegree[i] == 0:
            queue.append(i)
    
    # 큐가 빌 때까지
    while queue:
        now = queue.popleft()
        result.append(now)

        # 연결된 노드들 진입차수 -1
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    
    return result

# 하나의 테스트케이스 풀이
def solution():
    # 팀의 수, 작년 순위 저장
    N = int(input())
    last_rank = list(map(int, input().split()))
    
    # 그래프, 진입차수 저장
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for i in range(N):
        for j in range(i + 1, N):
            graph[last_rank[i]].append(last_rank[j])
            indegree[last_rank[j]] += 1
    
    # 상대 등수 변경 내용 저장 및 적용
    M = int(input())
    for i in range(M):
        a, b = map(int, input().split())
        if b in graph[a]:
            graph[a].remove(b)
            indegree[b] -= 1
            graph[b].append(a)
            indegree[a] += 1
        else:
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].append(b)
            indegree[b] += 1
    
    # 위상정렬 수행
    answer = topology_sort(graph, indegree)

    # 결과 출력
    if len(answer) == N:  # 모든 팀의 순위가 올바르게 정렬된 경우
        print(*answer)
    else:  # 모든 팀의 순위가 올바르게 나열되지 못한 경우
        print('IMPOSSIBLE')

T = int(input())  # 테스트케이스의 수
for _ in range(T):
    solution()