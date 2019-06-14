# 문제 4.
import random

x = random.randint(1, 9)
y = random.randint(1, 9)

# 문제
print(x, 'x', y, '=', '?')

# 보기 초기값 - 답 주입
s = set({x*y})

# 보기 내용
while len(s) != 9:
    s.add(random.randint(1, 9) * random.randint(1, 9))

# 보기 출력
for row in range(0, 3):
    for col in range(0, 3):
        print(s.pop(), end='\t')
    else:
        print()

answer = int(input('answer: '))

if x * y == answer:
    print('정답')
else:
    print('오답')