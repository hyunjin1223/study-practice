# 과목의 갯수
N = int(input())

# 
arr = list(map(int, input().split()))

# 최댓값
M = max(arr)

arr2 = 0

for i in arr:
    arr2 += i / M * 100
    
print(arr2 / N)
    