import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def main():
    inf = 10**20
    eps = 1.0 / 10**10
    mod = 10**9+7
    ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    dd = [(-1,0),(0,1),(1,0),(0,-1)]
    rr = []
    while True:
        n = I()
        if n == 0:
            break
        a = []
        for _ in range(n):
            a.append(LS())
        d = collections.defaultdict(int)
        ed = collections.defaultdict(lambda: None)
        for i in range(n):
            x, y, di = a[i]
            x = int(x)
            y = int(y)
            d[(x,y)] = i + 1
            if di == 'x':
                d[(x+1,y)] = i + 1
                ed[(x,y)] = (x+1,y)
                ed[(x+1,y)] = (x,y)
            else:
                d[(x,y+1)] = i + 1
                ed[(x,y)] = (x,y+1)
                ed[(x,y+1)] = (x,y)
        ee = collections.defaultdict(set)
        dka = list(d.keys())
        for x,y in list(d.keys()):
            dt = d[(x,y)]
            for di,dj in dd:
                ni = x + di
                nj = y + dj
                if d[(ni,nj)] > 0 and d[(ni,nj)] != dt:
                    ee[(x,y)].add((ni,nj))
        v = collections.defaultdict(bool)
        f = True
        for k in dka:
            if v[k]:
                continue
            s1 = set()
            s2 = set()
            ns1 = set([k])
            ns2 = set()
            while ns1 or ns2:
                s1 |= ns1
                na = list(ns1)
                ns1 = set()
                for k in na:
                    ns1 |= ee[k]
                    ns2.add(ed[k])
                ns2 -= s2
                na = list(ns2)
                s2 |= ns2
                ns2 = set()
                for k in na:
                    ns2 |= ee[k]
                    ns1.add(ed[k])
                ns1 -= s1
                ns2 -= s2
                s1 |= ns1
                s2 |= ns2
                if s1 & s2:
                    f = False
                    break
            if f:
                for k in s1:
                    v[k] = 1
                for k in s2:
                    v[k] = 1
            else:
                break
        if f:
            rr.append('Yes')
        else:
            rr.append('No')
    return '\n'.join(map(str,rr))
print(main())