import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import random
sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def main():
    q = I()
    aa = [LI() for _ in range(q)]
    bt = aa[0][2]
    m = 2 ** 20
    c = collections.defaultdict(int)
    lq = [inf]
    rq = [inf]
    c[-inf] = 1
    c[inf] = 1
    x = aa[0][1]
    c[x] = 1
    xl = 0
    lc = 0
    xr = 0
    rc = 0
    r = []
    for t in aa[1:]:
        if t[0] == 2:
            r.append('{} {}'.format(x, xl+xr+bt))
        else:
            _,a,b = t
            bt += b
            if a == x:
                c[x] += 1
                continue
            c[a] += 1
            if c[a] == 1:
                if a < x:
                    heapq.heappush(lq,-a)
                else:
                    heapq.heappush(rq,a)
            xc = c[x]
            if a < x:
                xl += x - a
                lc += 1
                t = xl + xr
                nx = -lq[0]
                nc = c[nx]
                s = x - nx
                nt = xl - lc * s + xr + (rc+xc) * s
                if nt <= t:
                    xl -= lc * s
                    xr += (rc+xc) * s
                    lc -= nc
                    rc += xc
                    heapq.heappush(rq,x)
                    x = nx
                    heapq.heappop(lq)
            else:
                xr += a - x
                rc += 1
                t = xl + xr
                nx = rq[0]
                nc = c[nx]
                s = nx - x
                nt = xl + (lc+xc) * s + xr - rc * s
                if nt < t:
                    xl += (lc+xc) * s
                    xr -= rc * s
                    lc += xc
                    rc -= nc
                    heapq.heappush(lq,-x)
                    x = nx
                    heapq.heappop(rq)
    return '\n'.join(r)
print(main())