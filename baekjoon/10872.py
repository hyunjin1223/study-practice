# problem: 10872
# tier: bronze
import sys

# 정수 N 입력 (0 <= N <= 12)
n = int(sys.stdin.readline())

# N! (팩토리얼) 계산
# 0!은 1임에 유의
result = 1

# 1부터 N까지 차례대로 곱함
for i in range(1, n + 1):
    result *= i

print(result)