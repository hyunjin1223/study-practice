# problem: 10952
# tier: bronze

while True:
    # 두 정수 입력
    A, B = map(int, input().split())
    
    # 0 0 입력 시 종료
    if A == 0 and B == 0:
        break
    
    # 두 수의 합 출력
    print(A + B)