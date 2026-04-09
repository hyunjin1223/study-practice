# problem: 8393
# tier: bronze

# n 입력
n = int(input())
total = 0

# 1부터 n까지 합산
for i in range(1, n + 1):
    total += i

# 결과 출력
print(total)