from collections import defaultdict, Counter
def scc(g):
    rg = defaultdict(list)
    fin = Counter()
    V = set()
    for u, e in g.items():
        V.add(u)
        for v in e:
            V.add(v)
            rg[v].append(u)
    o = []
    done = set()
    for v in V:
        if v in done:
            continue
        s = [(v, True)]
        while s:
            u, f = s.pop()
            if f:
                s.append((u, False))
                for v in g[u]:
                    if v in done:
                        continue
                    s.append((v, True))
                    done.add(v)
            else:
                o.append(u)
    done = set()
    ans = []
    while o:
        u = o.pop()
        if u in done:
            continue
        done.add(u)
        s = [u]
        vv = []
        while s:
            u  = s.pop()
            vv.append(u)
            for v in rg[u]:
                if v in done:
                    continue
                s.append(v)
                done.add(v)
        ans.append(vv)
    return ans
def atcoder_practice2_g():
    N, M = map(int, input().split())
    g = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        g[a].append(b)
    vv = scc(g)
    for r in vv:
        print(len(r), *r)
def test():
    g = {
        1: [2],
        5: [2],
        2: [4, 3],
        3: [4, 7, 6],
        4: [5, 8],
        6: [9],
        7: [8],
        8: [9],
        9: [7, 10],
        10: []
    }
    vv = scc(g)
    for r in vv:
        print(r)
if __name__ == "__main__":
    atcoder_practice2_g()