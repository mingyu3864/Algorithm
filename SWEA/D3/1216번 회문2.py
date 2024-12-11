import sys
sys.stdin = open("input.txt", "r")

def is_pal(arr, leng):
    for lst in arr:
        for i in range(N-leng+1):
            for j in range(leng//2):
                if lst[i+j] != lst[i+leng-1-j]:
                    break
            else:
                return True
    return False

T = 10
for tc in range(1, T+1):
    _ = input()
    N = 100
    arr1 = [input() for _ in range(N)] # 기존 배열
    arr2 = [''.join(x) for x in zip(*arr1)] # 전치 행렬

    for leng in range(N, 1, -1): # 찾으면 최대값
        if is_pal(arr1, leng) or is_pal(arr2, leng):
            break
    print(f"#{tc} {leng}")