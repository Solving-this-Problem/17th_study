# 17th_study
17주차 코딩테스트 준비

[백준 문제집](https://www.acmicpc.net/workbook/view/15895)
<br/><br/>
# 임스와 함께하는 미니게임
<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./W%EC%9E%84%EC%8A%A4%EC%99%80%20%ED%95%A8%EA%BB%98%ED%95%98%EB%8A%94%20%EB%AF%B8%EB%8B%88%EA%B2%8C%EC%9E%84/%EB%8F%99%EC%9A%B0.py)
```py
N, G = input().split()

n = int(N)
players = set()
for _ in range(n):
    player = input()
    players.add(player)

if G == 'Y':
    print(len(players))
elif G == 'F':
    print(len(players) // 2)
else:
    print(len(players) // 3)

```

## [민웅](./%EC%9E%84%EC%8A%A4%EC%99%80%20%ED%95%A8%EA%BB%98%ED%95%98%EB%8A%94%20%EB%AF%B8%EB%8B%88%EA%B2%8C%EC%9E%84/%EB%AF%BC%EC%9B%85.py)
```py
# 25757_임스와 함께하는 미니게임_ImsMinigame
import sys
input = sys.stdin.readline

games = {
    'Y': 2,
    'F': 3,
    'O': 4
}

N, G = input().split()
N = int(N)

max_user = games[G]
user_list = {}
count = 1
ans = 0

for _ in range(N):
    user = input()
    if user in user_list.keys():
        continue
    else:
        user_list[user] = 0
        count += 1
        if count == max_user:
            ans += 1
            count = 1

print(ans)
```
## [서희](./%EC%9E%84%EC%8A%A4%EC%99%80%20%ED%95%A8%EA%BB%98%ED%95%98%EB%8A%94%20%EB%AF%B8%EB%8B%88%EA%B2%8C%EC%9E%84/%EC%84%9C%ED%9D%AC.py)
```py
import sys
input = sys.stdin.readline

N, G = input().split()
player = [input() for _ in range(int(N))]
player = list(set(player))	# set 중복 제거

if G == 'Y' :	# 만약 게임 종류가 'Y'(윷놀이)라면, print(len(player))를 실행하여 참가 가능한 게임 횟수(참가자 수)를 출력
    print(len(player))
elif G == 'F' :	# 같은 그림 찾기
    print(len(player) // 2)
elif G == 'O' :	# 원카드
    print(len(player) // 3)
```
## [성구](./%EC%9E%84%EC%8A%A4%EC%99%80%20%ED%95%A8%EA%BB%98%ED%95%98%EB%8A%94%20%EB%AF%B8%EB%8B%88%EA%B2%8C%EC%9E%84/%EC%84%B1%EA%B5%AC.py)
```py
# 25757 임스와 함께하는 미니게임
import sys
input = sys.stdin.readline

player_limit={
    'Y': 1,
    'F': 2,
    'O': 3,
}

N, GameType = input().strip().split()
N = int(N)
players= [input().strip() for _ in range(N)]
played_players = set()
game_room = set()
limit = player_limit[GameType]
game_count = 0
count = 1
for player in players:
    count += 1
    if not player in played_players:
        played_players.add(player)
        game_room.add(player)
    if len(game_room) == limit:
        game_count += 1
        game_room.clear()
print(game_count)
        

#########
''' ㅋ 이게더 쉽고 빠름
import sys
input = sys.stdin.readline
N, GameType = input().strip().split()
players= {input().strip() for _ in range(int(N))}
player_num = len(players)
print(player_num if GameType == 'Y' else player_num//2 if GameType == 'F' else player_num//3)
'''
```
## [혜진](./%EC%9E%84%EC%8A%A4%EC%99%80%20%ED%95%A8%EA%BB%98%ED%95%98%EB%8A%94%20%EB%AF%B8%EB%8B%88%EA%B2%8C%EC%9E%84/%ED%98%9C%EC%A7%84.py)
```py
```

</div>
</details>
<br/><br/>

# 에디터

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./%EC%97%90%EB%94%94%ED%84%B0/%EB%8F%99%EC%9A%B0.py)
```py
# 어디가 틀린지 모르겠음 ㅠㅠ
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

# 민웅이형꺼 참고해서 풀었습니당
import sys
from collections import deque
input = sys.stdin.readline

s = list(input().strip())
s_tmp = deque()

M = int(input().strip())

for _ in range(M):
    order = input().strip()
    if order == 'L':
        if s:
            s_tmp.appendleft(s.pop())
    elif order == 'D':
        if s_tmp:
            s.append(s_tmp.popleft())
    elif order == 'B':
        if s:
            s.pop()
    else:
        s.append(order[-1])
print(''.join(s) + ''.join(s_tmp))

```
## [민웅](./%EC%97%90%EB%94%94%ED%84%B0/%EB%AF%BC%EC%9B%85.py)
```py
# 1406_에디터_Editor
# insert, remove는 시간초과
import sys
from collections import deque
input = sys.stdin.readline

alpha1 = list(input().rstrip())
alpha2 = deque()

M = int(input())
# idx = len(alpha1)

for _ in range(M):
    order, *new = input().split()
    if order == 'P':
        alpha1.append(new[0])
    elif order == 'L':
        if alpha1:
            alpha2.appendleft(alpha1.pop())
    elif order == 'D':
        if alpha2:
            alpha1.append(alpha2.popleft())
    else:
        if alpha1:
            alpha1.pop()
print(*alpha1, sep='', end='')
print(*alpha2, sep='')
```
## [서희](./%EC%97%90%EB%94%94%ED%84%B0/%EC%84%9C%ED%9D%AC.py)
```py
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
```
## [성구](./%EC%97%90%EB%94%94%ED%84%B0/%EC%84%B1%EA%B5%AC.py)
```py
# 1406 에디터, 37576KB, 364ms, Python
import sys
input = sys.stdin.readline

str_stack = list(input().strip())
# print("string is", str_stack)
stack = []
def L():
    global str_stack
    # print("L", place)
    if not str_stack:
        return
    stack.append(str_stack.pop())
    return

def D():
    global str_stack, stack
    # print("D", place)
    if not stack:
        return
    str_stack.append(stack.pop())
    return

def B():
    global str_stack
    # print("B", place)
    if not str_stack:
        return
    # string.pop(place-1)
    str_stack.pop()
    return

def P(character):
    global str_stack
    # print("P, character = ", character, place)
    str_stack.append(character)
    return 


# print("Place is ", place)
for _ in range(int(input())):
    order = list(input().strip().split())
    if order[0] == "L":
        L()
    elif order[0] == "D":
        D()
    elif order[0] == "B":
        B()
    else:
        P(order[1])
    # print("String is", str_stack, "\nstack is", stack)
# print("".join(string))
print("".join(str_stack)+"".join(stack[::-1]))
        
```
## [혜진](./%EC%97%90%EB%94%94%ED%84%B0/%ED%98%9C%EC%A7%84.py)
```py
```

</div>
</details>

<br/><br/>

# 공유기 설치

<details>
<summary>접기/펼치기</summary>
<div markdown="1">


## [동우](./%EA%B3%B5%EC%9C%A0%EA%B8%B0%20%EC%84%A4%EC%B9%98/%EB%8F%99%EC%9A%B0.py)
```py
```
## [민웅](./%EA%B3%B5%EC%9C%A0%EA%B8%B0%20%EC%84%A4%EC%B9%98/%EB%AF%BC%EC%9B%85.py)
```py
# 2110_공유기설치_Install-router
# 알고리즘 구분 참조했음
import sys
input = sys.stdin.readline

N, C = map(int, input().rstrip().split())

houses = []
ans = 0
for _ in range(N):
    houses.append(int(input()))

houses.sort()

# 공유기가 2개면 무조건 정렬된 상태의 양 끝
if C == 2:
    ans = houses[N-1] - houses[0]
# 3개 이상일 경우 가능한 최대 거리의 절반부터 이분탐색으로 원하는 공유기 개수만큼 설치가가능한지 판단
else:
    min_dis = 1
    max_dis = houses[N-1] - houses[0]
    while min_dis <= max_dis:
        cnt = 0
        router = houses[0]
        mid = (min_dis + max_dis)//2

        for i in range(1, N):
            if houses[i]-mid >= router:
                cnt += 1
                router = houses[i]
        if cnt >= C-1:
            min_dis = mid + 1
            ans = mid
        else:
            max_dis = mid - 1
print(ans)

```
## [서희](./%EA%B3%B5%EC%9C%A0%EA%B8%B0%20%EC%84%A4%EC%B9%98/%EC%84%9C%ED%9D%AC.py)
```py
```
## [성구](./%EA%B3%B5%EC%9C%A0%EA%B8%B0%20%EC%84%A4%EC%B9%98/%EC%84%B1%EA%B5%AC.py)
```py
import sys
input = sys.stdin.readline


N, C = map(int, input().split())
house = sorted([int(input()) for _ in range(N)])

if C == 2:
    print(house[N-1] - house[0])
else:
    start, end = 1, house[N-1]-house[0]
    
    while end > start:
        count = 1
        mid = (end+start)//2
        pivot = house[0]
        for i in range(N):
            if house[i] - pivot >= mid:
                count += 1
                pivot = house[i]
        if count >= C:
            ans = mid
            start = mid + 1
        else:
            end = mid

    print(ans)

```
## [혜진](./%EA%B3%B5%EC%9C%A0%EA%B8%B0%20%EC%84%A4%EC%B9%98/%ED%98%9C%EC%A7%84.py)
```py
```

</div>
</details>
