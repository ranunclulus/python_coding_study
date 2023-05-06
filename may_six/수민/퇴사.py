# 퇴사 날짜 입력 받기
n = int(input())
array = [[]]

# 상담 일정표 입력 받기
for _ in range(n):
    array.append(list(map(int, input().split())))

# dp테이블 => d[i] : i일부터 마지막 날까지 완료할 수 있는 상담의 금액 최댓값을 저장
d = [0] * (n+1)

# 상담 마지막 날만 미리 값 채우기
if n + array[n][0] > n+1: # 상담에 걸리는 기간이 일정보다 넘어가는 경우
    d[n] = 0
else: # 넘어가지 않는 경우 해당 날 금액 저장
    d[n] = array[n][1]

# 다이나믹 프로그래밍
for i in range(n-1, 0, -1): # 상담 마지막 날 전날 부터 1일까지 계산
    time = array[i][0]
    cost = array[i][1]
    # 해당 i일의 상담 기간이 주어진 퇴사일보다 넘어가는 경우
    if time + i> n+1: 
        d[i] = d[i+1] # 이전 값의 최댓값을 저장
    # 해당 i일의 상담 기간이 주어진 퇴사일보다 넘어가지 않는 경우
    else:
        if i + time <= n:
            d[i] = max(cost + d[i + time], d[i+1]) # 이전 값의 최댓값과 i날의 상담을 진행해 얻은 최댓값 중 큰 값을 저장
        else: # 인덱스 벗어나는 경우
            d[i] = max(cost ,d[i+1])
print(d[1])
