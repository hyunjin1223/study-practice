# problem: 9506
# tier: bronze

while True:
    n = int(input())
    if n == -1:
        break
    
    # 약수 찾기 (자기 자신 제외)
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    
    # 약수들의 합이 n과 같은지 확인 (완전수 판정)
    if sum(divisors) == n:
        # 출력 형식: n = 1 + 2 + 3...
        print(f"{n} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{n} is NOT perfect.")