N = int(input())  # 도시의 개수
graph = [list(map(int, input().split())) for _ in range(N)]  # 도시 간의 최소 이동 시간

# 출발지와 도착지 사이 도로가 필수인 경우 소요 시간 반환
def find_essential_road(start, end):
    for middle in range(N):
        # 경유지가 출발지 또는 도착인 경우 통과
        if middle == start or middle == end:
            continue
        # 필수 도로인지 확인할 수 없는 경우
        if graph[start][end] > graph[start][middle] + graph[middle][end]:
            return -1
        # 필수 도로가 아닌 경우
        elif graph[start][end] == graph[start][middle] + graph[middle][end]:
            return 0
    return graph[start][end]

# 모든 필수 도로의 시간의 합 반환
def solution():
    result = 0
    for start in range(N):
        for end in range(N):
            # 출발지와 도착지가 동일한 경우 통과
            if start == end:
                continue
            
            time = find_essential_road(start, end)
            if time == -1:
                return -1
            result += time
    
    return result // 2  # 도로의 시간 합 반환(양방향 확인했기 때문에 절반)

print(solution())  # 결과 출력