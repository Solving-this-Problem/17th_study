import sys
input = sys.stdin.readline

# 입력파트
N, C = map(int, input().split())
house = sorted([int(input()) for _ in range(N)])


# 2개 설치할 경우 무조건 양 끝
if C == 2:
    print(house[N-1] - house[0])
else:
    # 거리를 기준으로 처음과 끝을 세팅
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
