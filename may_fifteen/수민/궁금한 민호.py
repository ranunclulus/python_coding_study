import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

check = [[1] * n for _ in range(n)]
result = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            # 비교할 필요 없는 경우는 pass
            if a == b or b == k or a == k: 
                continue
            # k노드를 거쳐가는 경우가 최단 거리일 때 a랑 b 연결하는 간선이 필요없음
            if graph[a][b] == graph[a][k] + graph[k][b]:
                check[a][b] = 0
            # 이 경우는 아예 불가능
            elif graph[a][b] > graph[a][k] + graph[k][b]:
                result = -1

if result != -1:
    for i in range(n):
        for j in range(i, n):
            if check[i][j]: 
                result += graph[i][j]
print(result)