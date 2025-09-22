def solve(n, t, ab_list):
    a0b_list = [ab[1] for ab in ab_list if ab[0] == 0]
    apb_list = []
    for ab in ab_list:
        if ab[0] > 0:
            apb_list.append(ab)
    a0b_list = sorted(a0b_list)
    apb_list = sorted(apb_list, key=lambda x: - x[0] / (x[1] + 1))
    m = len(apb_list)
    dp = [[t + 1] * 30 for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 0
    for i in range(m):
        for k in range(1, 30):
            ti = dp[i][k - 1] + 1
            a, b = apb_list[i]
            dp[i + 1][k] = min(dp[i][k], ti + a * ti + b)
    a0b_list_cum_sum = [0]
    s = 0
    for b in a0b_list:
        s += b + 1
        a0b_list_cum_sum.append(s)
    res = 0
    for k in range(len(a0b_list_cum_sum)):
        for p in range(30):
            if dp[m][p] + a0b_list_cum_sum[k] <= t:
                res = max(res, k + p)
    return res
def main():
    n, t = map(int, input().split())
    ab_list = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, t, ab_list)
    print(res)
def test():
    assert solve(3, 7, [[2, 0], [3, 2], [0, 3]]) == 2
    assert solve(1, 3, [[0, 3]]) == 0
    assert solve(5, 21600, [[2, 14], [3, 22], [1, 3], [1, 10], [1, 9]]) == 5
if __name__ == "__main__":
    test()
    main()