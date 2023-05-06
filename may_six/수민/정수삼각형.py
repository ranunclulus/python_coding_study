n = int(input())
# 정수 삼각형 숫자 배열에 저장
d = []
for _ in range(n):
    d.append(list(map(int, input().split())))
    
# 배열 아래에서 부터 값 채워 넣기
for i in range(len(d)-2, -1, -1):
    for j in range(0, i+1):
        # 아래 대각선 왼쪽과 오른쪽 값 중 큰 값을 골라 해당 값과 더한 값으로 update
        d[i][j] = max(d[i+1][j], d[i+1][j+1]) + d[i][j]
print(d[0][0])
