import sys
sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7
def input():
    return sys.stdin.readline().strip()
def main():
    H, W = map(int, input().split())
    A = []
    cnt = 0
    for _ in range(H):
        a = list(map(int, input().split()))
        cnt += sum(a)
        A.append(a)
    ans = []
    for h in range(H):
        if h % 2 == 0:
            for w in range(W):
                if h == H - 1 and w == W - 1:
                    continue
                if A[h][w] % 2 == 1:
                    if w == W - 1:
                        A[h][w] -= 1
                        A[h + 1][w] += 1
                        ans.append((h, w, h + 1, w))
                    else:
                        A[h][w] -= 1
                        A[h][w + 1] += 1
                        ans.append((h, w, h, w + 1))
                else:
                    continue
        else:
            for w in range(W)[::-1]:
                if h == H - 1 and w == 0:
                    continue
                if A[h][w] % 2 == 1:
                    if w == 0:
                        A[h][w] -= 1
                        A[h + 1][w] += 1
                        ans.append((h, w, h + 1, w))
                    else:
                        A[h][w] -= 1
                        A[h][w - 1] += 1
                        ans.append((h, w, h, w - 1))
                else:
                    continue
    print(len(ans))
    for a, b, c, d in ans:
        print(a + 1, b + 1, c + 1, d + 1)
if __name__ == "__main__":
    main()