# problem: 3003
# tier: bronze

# 정답 기물 개수
correct = [1, 1, 2, 2, 2, 8]

# 현재 기물 개수 입력
pieces = list(map(int, input().split()))

# 차이 계산 및 출력
for i in range(6):
    print(correct[i] - pieces[i], end=" ")