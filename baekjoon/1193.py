# problem: 1193
# tier: silver

X = int(input())
line = 1

# 사선 라인 탐색
while X > line:
    X -= line
    line += 1

# 짝수 라인: 위에서 아래로 (분자 증가)
if line % 2 == 0:
    up = X
    down = line - X + 1
# 홀수 라인: 아래에서 위로 (분모 증가)
else:
    up = line - X + 1
    down = X

print(f"{up}/{down}")