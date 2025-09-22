import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def main():
    rr = []
    n = I()
    ni = 0
    while ni < n:
        ni += 1
        a = []
        while len(a) < 9:
            a += LS()
        t = int(a[-1],16)
        a = list(map(lambda x: int(x,16), a[:-1]))
        r = 0
        for i in range(32):
            ii = 2**i
            iii = 2**(i+1)
            b = t & ii
            c = 0
            for d in a:
                c += d^r
            if (c & ii) != b:
                r += ii
        rr.append('{:0x}'.format(r))
    return '\n'.join(map(str, rr))
print(main())