import sys
sys.stdin = open("input.txt", "r")

def count(arr):
    ret = 0
    for lst in arr:
        cnt = 0
        for j in range(len(lst)):
            if lst[j]: # 값이 0이 아닌경우
                cnt += 1
            else:
                if cnt == K:
                    ret += 1
                cnt = 0
    return ret

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
    arr_t = list(map(list, zip(*arr))) # 전치행렬
    ans = count(arr) + count(arr_t)
    print(f"#{tc} {ans}")