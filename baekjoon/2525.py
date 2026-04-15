# problem: 2525
# tier: bronze

# 현재 시(H), 분(M) 입력
H, M = map(int, input().split())
# 소요 시간(M2) 입력
M2 = int(input())

# 1. 분 단위 합산
M += M2

# 2. 60분을 초과하는 만큼 시(H)에 가산
H += M // 60

# 3. 분(M)을 60으로 나눈 나머지로 갱신
M %= 60

# 4. 시(H)를 24시간 체계로 변환 (24시 → 0시)
H %= 24

# 종료 시간 출력
print(H, M)