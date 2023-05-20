n = int(input())

# 좌표 입력받기
coordinate = [[0]]
for i in range(n):
    x, y, z = map(int, input().split())
    coordinate.append((x, y, z))

# 부모 노드 초기화
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

# 부모 노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 연결해 주기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 좌표값 중 가장 최소의 절대값 반환
def find_min(coordinate, a, b):
    xabs = abs(coordinate[a][0] - coordinate[b][0])
    yabs = abs(coordinate[a][1] - coordinate[b][1])
    zabs = abs(coordinate[a][2] - coordinate[b][2])
    return min(xabs, yabs, zabs)

# 간선 만들어 주기
edges = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i == j):
            break
        a = find_parent(parent, i)
        b = find_parent(parent, j)
        if (a != b):
            cost = find_min(coordinate, i, j)
            edges.append((cost, i, j))
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)