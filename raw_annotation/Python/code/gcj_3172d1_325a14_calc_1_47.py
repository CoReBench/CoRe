def calc(n, d, a, b, ct):
    n = len(a)
    ans = d - 1
    ret = a[0]
    for i in range(n):
        x, y = a[i], b[i]
        cur_d = 0
        p = 0
        cut = 0
        for j in range(d + 2):
            p += x
            tmp = ct.get(p, 0)
            remain_d = d - cur_d
            per_d = p/x
            per_cut = per_d - 1
            for k in range(tmp*per_d):
                cur_d += 1
                if (k+1) % per_d != 0:
                    cut += 1
                xx = d/cur_d
                if d % cur_d == 0:
                    xx -= 1
                ans = min(ans, cut + xx*cur_d)
                if cur_d > d:
                    break
            if cur_d > d:
                break
        if cur_d < d:
            for j in range(n-1, i, -1):
                if a[j] > p or a[j] % x != 0:
                    tmp = (a[j]/x) * y
                    for k in range(tmp):
                        cur_d += 1
                        cut += 1
                        xx = d/cur_d
                        if d % cur_d == 0:
                            xx -= 1
                        ans = min(ans, cut + xx*cur_d)
                        if cur_d > d:
                            break
                if cur_d > d:
                    break
        xx = d/cur_d
        if d%cur_d == 0:
            xx -= 1
        ans = min(ans, cut + xx * cur_d)
    return (ans, ret)
def work(case):
    n, d = raw_input().strip().split()
    n, d = int(n), int(d)
    tmp = [int(i) for i in raw_input().strip().split()]
    ct = dict([(i, 0) for i in tmp])
    for i in tmp:
        ct[i] += 1
    a, b = zip(*sorted(ct.items()))
    ans, ret = calc(n, d, a, b, ct)
    print('Case #%d: %d' % (case, ans))
if __name__ == '__main__':
    T = int(raw_input())
    for i in range(T):
        work(i+1)