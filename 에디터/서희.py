import sys
from collections import deque

S = list(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())

left = deque(S) # 모든 문자들이 커서의 왼쪽에 있으므로, 모든 문자들이 왼쪽 스택에 저장
right = deque()

for _ in range(C):
    c = sys.stdin.readline().split()

    if c[0] == 'L' and left:
        right.appendleft(left.pop())
    elif c[0] == 'D' and right:
        left.append(right.popleft())
    elif c[0] == 'B' and left:
        left.pop()
    elif c[0] == 'P':
        left.append(c[1])

print(''.join(left + right))
