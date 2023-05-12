## 📢시간 초과 해결 못했습니다!!ㅠㅠ

import sys

input = sys.stdin.readline
INF = int(1e9)

# 벨만 포드 알고리즘
def bf(start):
    distance = [INF] * (n+1)
    distance[start]=0

    for i in range(n):
        for j in range(len(edges)):
            cur = edges[j][0]
            next = edges[j][1]
            cost = edges[j][2]

            if distance[cur] != INF and distance[next] > cost + distance[cur]:
                distance[next] = cost + distance[cur]
                if i == n - 1:
                    return True

    return False


t = int(input())

for _ in range(t):
    # 지점수, 도로수, 웜홀수
    n, m, w = map(int, input().split())
    edges = []

    # 도로 정보
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    # 웜홀 정보
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    result = False

    for i in range(1,n+1):
        if bf(i):
            result = True
            break
    if result:
        print("YES")
    else:
        print("NO")