from collections import defaultdict
def solve(n, k, a_list):
    b_list = [a - 1 for a in a_list]
    res_dict = defaultdict(list)
    res_dict[0].append(0)
    r = 0
    for i in range(n):
        r += b_list[i]
        r %= k
        res_dict[r].append(i + 1)
    res = 0
    for r in res_dict.keys():
        r_list = res_dict[r]
        if len(r_list) == 1:
            continue
        i = 0
        j = 0
        while i < len(r_list) - 1:
            if j < len(r_list) - 1:
                while r_list[j + 1] - r_list[i] < k:
                    j += 1
                    if j == len(r_list) - 1:
                        break
            res += j - i
            i += 1
    return res
def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)
def test():
    assert solve(5, 4, [1, 4, 2, 3, 5]) == 4
    assert solve(8, 4, [4, 2, 4, 2, 4, 2, 4, 2]) == 7
    assert solve(10, 7, [14, 15, 92, 65, 35, 89, 79, 32, 38, 46]) == 8
if __name__ == "__main__":
    main()