# problem: 24723
# tier: bronze
import sys

# 녹색 거탑의 높이 N 입력
n = int(sys.stdin.readline())

# 각 층에서 내려갈 수 있는 방향은 왼쪽 또는 오른쪽 두 가지임
# 1층: 2가지
# 2층: 2 * 2 = 4가지
# N층: 2^N 가지 경로가 존재함
print(2**n)