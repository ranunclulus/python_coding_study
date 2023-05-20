import sys

input = sys.stdin.readline

def get_distance(locationA, locationB):
    return min(abs(locationA[0] - locationB[0]), abs(locationA[1] - locationB[1]), abs(locationA[2] - locationB[2]))

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

N = int(input())  # 행성의 개수
planets = [list(map(int, input().split())) + [i] for i in range(N)]  # 행성들의 x, y, z 좌표

planetsX = sorted(planets, key=lambda x:x[0])  # 행성의 x 좌표를 기준으로 오름차순 정렬
planetsY = sorted(planets, key=lambda x:x[1])  # 행성의 y 좌표를 기준으로 오름차순 정렬
planetsZ = sorted(planets, key=lambda x:x[2])  # 행성의 z 좌표를 기준으로 오름차순 정렬

tunnels = []  # 행성 터널 정보 (출발지, 도착지, 연결 최소 비용)
for i in range(N - 1):
    tunnels.append((planetsX[i][3], planetsX[i + 1][3], abs(planetsX[i][0] - planetsX[i + 1][0])))
    tunnels.append((planetsY[i][3], planetsY[i + 1][3], abs(planetsY[i][1] - planetsY[i + 1][1])))
    tunnels.append((planetsZ[i][3], planetsZ[i + 1][3], abs(planetsZ[i][2] - planetsZ[i + 1][2])))
tunnels.sort(key=lambda x:x[2])  # 연결 비용을 기준으로 오름차순 정렬

parent = [i for i in range(N)]  # 행성들의 부모 노드

result = 0
for tunnel in tunnels:
    start, end, cost = tunnel  # 출발지, 도착지, 연결 최소 비용

    # 출발지와 도착지가 연결이 안된 경우 연결
    if find_parent(parent, start) != find_parent(parent, end):
        union_parent(parent, start, end)
        result += cost

print(result)  # 결과 출력