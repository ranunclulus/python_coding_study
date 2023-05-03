n = int(input())
d = []
for _ in range(n):
    d.append(list(map(int, input().split())))
for i in range(len(d)-2, -1, -1):
    for j in range(0, i+1):
        d[i][j] = max(d[i+1][j], d[i+1][j+1]) + d[i][j]
print(d[0][0])