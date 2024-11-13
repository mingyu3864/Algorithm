import sys
sys.stdin = open("input.txt", "r")

nums = [2, 3, 5, 7, 11]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnts = [0] * 5
    for i in range(5):
        # nums의 숫자로 나누어 떨어진다면 cnt 증가
        while N % nums[i] == 0:
            cnts[i] += 1
            N /= nums[i]
    print(f"#{tc}", *cnts)