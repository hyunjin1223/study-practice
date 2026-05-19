# problem: 5622
# tier: bronze

# 단어 입력
word = input()

# 다이얼 알파벳 배열 (0, 1번 제외, 2번부터 시작)
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

total_time = 0

# 단어의 각 문자가 어떤 다이얼에 속하는지 확인
for char in word:
    for i in range(len(dial)):
        if char in dial[i]:
            # 다이얼 숫자 + 1초 (2번 다이얼은 3초 소요되므로 index + 3)
            total_time += (i + 3)

# 결과 출력
print(total_time)