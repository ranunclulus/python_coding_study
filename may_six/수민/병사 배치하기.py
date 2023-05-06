# 병사의 수 입력 받기
n = int(input())

# 병사 전투력 입력 받기
array = list(map(int, input().split()))

# dp 테이블 => d[i] : i번째 array 값을 마지막 원소로 하는 감소하는 부분 수열의 길이 최댓값을 저장
d = [1] * n 

# 감소하는 부분 수열의 길이 최댓값 구하기(다이나믹 프로그래밍)
for i in range(n):
    for j in range(i): # 해당 값 앞 부분 d배열 중 큰 값을 골라서 1 더한 값 중 최댓값을 저장
        if array[j] > array[i]:
            d[i] = max(d[i], d[j] + 1)
print(n-max(d))