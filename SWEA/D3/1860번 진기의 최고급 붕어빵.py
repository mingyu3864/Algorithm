import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    ans = "Possible"
    cnt = 0
    for i in lst:
        cnt += 1
        if (i//M)*K < cnt:
            ans = "Impossible"
            break
    print(f"#{tc} {ans}")