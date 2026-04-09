# problem: 3052
# tier: bronze

# 서로 다른 나머지를 저장할 집합(set) 생성
arr = set()

# 10개의 수를 입력받는 반복문
for _ in range(10):
    num = int(input())       # 숫자 입력
    arr.add(num % 42)        # 42로 나눈 나머지를 집합에 추가 (중복 자동 제거)
 
# 집합의 크기 = 서로 다른 나머지의 개수 
print(len(arr))