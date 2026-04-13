# problem: 2739
# tier: bronze

# 단 수(N) 입력
N = int(input())

# 1부터 9까지 곱셈 결과 출력
for i in range(1, 10):
    print(f"{N} * {i} = {N * i}")