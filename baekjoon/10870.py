# problem: 10870
# tier: bronze
import sys

# n번째 피보나치 수를 구하는 문제 (0 <= n <= 20)
# 피보나치 수 공식: Fn = Fn-1 + Fn-2 (n ≥ 2)
n = int(sys.stdin.readline())

def fibonacci(k):
    # 기본 케이스: 0번째는 0, 1번째는 1
    if k == 0:
        return 0
    if k == 1:
        return 1
    # 재귀 호출을 통한 피보나치 계산
    return fibonacci(k - 1) + fibonacci(k - 2)

print(fibonacci(n))