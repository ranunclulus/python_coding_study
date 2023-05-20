import sys

input = sys.stdin.readline

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())  # 집의 개수, 길의 개수
roads = []  # 길 정보
for _ in range(M):
    roads.append(tuple(map(int, input().split())))
roads.sort(key=lambda x:x[2])  # 길 유지비 기준으로 오름차순 정렬

parent = [i for i in range(N + 1)]  # 집의 부모 노드

result = 0  # 두 마을의 길 유지비
last = 0  # 마지막에 연결한 길 유지비
for road in roads:
    start, end, cost = road

    # 연결된 집이 아닌 경우
    if find_parent(parent, start) != find_parent(parent, end):
        union_parent(parent, start, end)  # 길 연결
        result += cost  # 길 비용 추가
        last = cost  # 마지막 연결 길 갱신

print(result - last)  # 결과 출력