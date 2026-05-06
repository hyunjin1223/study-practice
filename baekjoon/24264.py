# problem: 24264
# tier: bronze

# MenOfPassion(A, n) {
#     sum <- 0;
#     for i from 1 to n
#         for j from 1 to n
#             sum <- sum + A[i] * A[j]; # 코드1
#     return sum;
# }

n = int(input())

# 중첩 반복문으로 n * n번 실행됨
print(n * n)
# n^2 이므로 차수는 2 (이차 시간 복잡도 O(n^2))
print(2)