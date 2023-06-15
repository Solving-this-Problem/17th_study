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
```

## [민웅](./%EC%9E%84%EC%8A%A4%EC%99%80%20%ED%95%A8%EA%BB%98%ED%95%98%EB%8A%94%20%EB%AF%B8%EB%8B%88%EA%B2%8C%EC%9E%84/%EB%AF%BC%EC%9B%85.py)
```py
```
## [서희](./%EC%9E%84%EC%8A%A4%EC%99%80%20%ED%95%A8%EA%BB%98%ED%95%98%EB%8A%94%20%EB%AF%B8%EB%8B%88%EA%B2%8C%EC%9E%84/%EC%84%9C%ED%9D%AC.py)
```py
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
```
## [민웅](./%EC%97%90%EB%94%94%ED%84%B0/%EB%AF%BC%EC%9B%85.py)
```py
```
## [서희](./%EC%97%90%EB%94%94%ED%84%B0/%EC%84%9C%ED%9D%AC.py)
```py
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
```
## [서희](./%EA%B3%B5%EC%9C%A0%EA%B8%B0%20%EC%84%A4%EC%B9%98/%EC%84%9C%ED%9D%AC.py)
```py
```
## [성구](./%EA%B3%B5%EC%9C%A0%EA%B8%B0%20%EC%84%A4%EC%B9%98/%EC%84%B1%EA%B5%AC.py)
```py
```
## [혜진](./%EA%B3%B5%EC%9C%A0%EA%B8%B0%20%EC%84%A4%EC%B9%98/%ED%98%9C%EC%A7%84.py)
```py
```

</div>
</details>