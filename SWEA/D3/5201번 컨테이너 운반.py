import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    # 내림차순 정렬
    wi.sort(reverse = True)
    ti.sort(reverse = True)

    # 짐을 하나씩 내리면서 트럭에 적재 가능 체크
    cnt = i = 0
    for w in wi: # 화물 한개씩
        if w <= ti[i]: # 가능
            cnt += w
            i += 1
            if i == M: # 트럭이 없는 경우 => 종료
                break

    print(f"#{tc} {cnt}")