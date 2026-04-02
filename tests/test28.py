# 배구니 갯수를 N, 역순으로 바꾸는 횟수를 M
N, M = map(int, input().split())

# 
arr = list(range(1, N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    arr[i-1:j] = arr[i-1:j][::-1]
    
print(*arr)
    
    






































