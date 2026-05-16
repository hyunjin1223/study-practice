# problem: 10798
# tier: bronze

# 5개의 줄을 입력받아 리스트에 저장
words = []
for _ in range(5):
    words.append(input())

# 최대 길이는 15이므로 15번 반복하며 세로로 읽기
for j in range(15):
    for i in range(5):
        # 현재 행(i)의 문자열 길이가 열 번호(j)보다 클 때만 출력
        if j < len(words[i]):
            print(words[i][j], end='')