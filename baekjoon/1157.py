# problem: 1157
# tier: bronze

# 단어 입력 및 대문자로 변환
word = input().upper()
# 중복 제거된 알파벳 리스트
unique_words = list(set(word))

cnt_list = []
for x in unique_words:
    # 각 알파벳이 단어에서 몇 번 나오는지 카운트
    cnt = word.count(x)
    cnt_list.append(cnt)

# 가장 많이 나온 횟수가 여러 개인지 확인
if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    # 가장 많이 나온 알파벳 출력
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])