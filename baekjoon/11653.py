# problem: 11653
# tier: bronze

N = int(input())

# 1은 소인수분해를 하지 않음
if N == 1:
    exit()

# 2부터 시작하여 나누어 떨어지는지 확인
d = 2
while d * d <= N:
    if N % d == 0:
        print(d)
        N //= d
    else:
        d += 1

# 마지막으로 남은 소수 출력
if N > 1:
    print(N)