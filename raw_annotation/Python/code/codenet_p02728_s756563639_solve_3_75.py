from collections import deque
MOD = 10 ** 9 + 7
def solve(n, edge_list):
    factorial = [1] * n
    for i in range(1, n):
        factorial[i] = (factorial[i - 1] * i) % MOD
    factorial_inv = [1] * n
    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)
    for i in range(n - 2, 0, -1):
        factorial_inv[i] = (factorial_inv[i + 1] * (i + 1)) % MOD
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = edge_list[i]
        g[a].append(b)
        g[b].append(a)
    order = []
    parent = [-1] * n
    parent[0] = 0
    children = [[] for _ in range(n)]
    queue = deque([0])
    while len(queue) > 0:
        p = queue.popleft()
        order.append(p)
        for q in g[p]:
            if parent[q] == -1:
                parent[q] = p
                children[p].append(q)
                queue.append(q)
    count_children_res = [-1] * n
    for x in order[::-1]:
        if len(children[x]) == 0:
            count_children_res[x] = 0
        else:
            total = 0
            for y in children[x]:
                total += count_children_res[y]
            r = len(children[x]) + total
            count_children_res[x] = r
    assign_children_res = [-1] * n
    for x in order[::-1]:
        if len(children[x]) == 0:
            assign_children_res[x] = 1
        else:
            r = factorial[count_children_res[x]]
            for y in children[x]:
                r *= assign_children_res[y]
                r *= factorial_inv[count_children_res[y] + 1]
                r %= MOD
            assign_children_res[x] = r
    assign_parents_res = [-1] * n
    assign_parents_res[0] = 1
    for x in order[1:]:
        p = parent[x]
        r = assign_children_res[p]
        r *= pow(assign_children_res[x], MOD - 2, MOD)
        r *= factorial[count_children_res[x] + 1]
        r *= factorial_inv[count_children_res[p]]
        r *= assign_parents_res[p]
        r *= factorial[n - count_children_res[x] - 2]
        r *= factorial_inv[n - count_children_res[p] - 1]
        r %= MOD
        assign_parents_res[x] = r
    res_list = [0] * n
    res_list[0] = assign_children_res[0]
    for i in range(1, n):
        res = factorial[n - 1]
        for j in children[i]:
            res *= assign_children_res[j]
            res *= factorial_inv[count_children_res[j] + 1]
            res %= MOD
        res *= assign_parents_res[i]
        res *= factorial_inv[n - 1 - count_children_res[i]]
        res %= MOD
        res_list[i] = res
    return res_list
def main():
    n = int(input())
    edge_list = []
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edge_list.append((a - 1, b - 1))
    res_list = solve(n, edge_list)
    for res in res_list:
        print(res)
def test():
    assert solve(3, [(0, 1), (0, 2)]) == [2, 1, 1]
    assert solve(2, [(0, 1)]) == [1, 1]
    assert solve(5, [(0, 1), (1, 2), (2, 3), (2, 4)]) == [2, 8, 12, 3, 3]
    assert solve(8, [(0, 1), (1, 2), (2, 3), (2, 4), (2, 5), (5, 6), (5, 7)]) == [40, 280, 840, 120, 120, 504, 72, 72]
if __name__ == "__main__":
    test()
    main()