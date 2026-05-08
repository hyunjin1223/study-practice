# problem: 24265
# tier: bronze

# MenOfPassion(A, n) {
#     sum <- 0;
#     for i from 1 to n - 1
#         for j from i + 1 to n
#             sum <- sum + A[i] * A[j]; # 코드1
#     return sum;
# }

n = int(input())

# i가 1일 때 j는 2~n (n-1번)
# i가 2일 때 j는 3~n (n-2번)
# ... i가 n-1일 때 j는 n (1번)
# 총 합: (n-1) + (n-2) + ... + 1 = n*(n-1)/2
print(n * (n - 1) // 2)
# n^2에 비례하므로 차수는 2
print(2)