# Problem: 3003
# Tier: Bronz

# 정답 기물 개수 (문제에서 주어진 값)
correct = [1, 1, 2, 2, 2, 8]

# 현재 가지고 있는 기물 개수 입력받기
pieces = list(map(int, input().split()))

# 각 기물마다 부족/초과 개수 계산해서 출력
for i in range(6):
    # 정답 - 현재 개수
    print(correct[i] - pieces[i], end=" ")