import sys


def L():
    global cnt
    if cnt != 0:
        cnt -= 1


def D():
    global cnt
    if cnt != len(s):
        cnt += 1


def B():
    global cnt
    if len(s) != 0:
        for _ in range(cnt):
            s.pop(0)
            cnt = len(s)


s = list(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

cnt = len(s)
for _ in range(M):
    order = sys.stdin.readline().strip()
    if order == 'L':
        L()
    elif order == 'D':
        D()
    elif order == 'B':
        B()
    else:
        s.insert(cnt, order[-1])
        cnt += 1
print(''.join(s))