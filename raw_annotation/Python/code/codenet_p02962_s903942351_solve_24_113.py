from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.buffer.readline().split()]
def I(): return int(sys.stdin.buffer.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]
sys.setrecursionlimit(1000000)
def solve():
    mod = 1000000007
    s = S()
    t = S()
    ns = len(s)
    nt = len(t)
    f = {}
    for i in range(26):
        f[chr(i + ord("a"))] = i + 1
    for i in range(ns):
        s[i] = f[s[i]]
    for i in range(nt):
        t[i] = f[t[i]]
    b = 10
    mod1 = 1000000007
    mod2 = 1000000009
    pownt1 = pow(b,nt,mod)
    invnt1 = pow(pownt1,mod1-2,mod1)
    powns1 = pow(b,ns,mod1)
    invns1 = pow(powns1,mod1-2,mod1)
    pownt2 = pow(b,nt,mod2)
    invnt2 = pow(pownt2,mod2-2,mod2)
    powns2 = pow(b,ns,mod2)
    invns2 = pow(powns2,mod2-2,mod2)
    l = 0
    r = ns+2
    while r > l+1:
        m = (l+r) >> 1
        n = m*nt
        st = [m]*nt
        ms = n//ns
        rs = n-ms*ns
        ss = []
        for i in range(ns):
            if i < rs:
                ss.append(ms + 1)
            else:
                ss.append(ms)
        p1 = pow(b,n,mod1)
        p2 = pow(b,n,mod2)
        h1 = 0
        h2 = 0
        for i in range(nt):
            ti = t[i]
            pow1 = pow(b,(n-i)*mod1,mod1)
            pows1 = pow(pownt1,st[i],mod1)
            h1 += ti*pow1*(pows1-1)*pow(pows1*(1-invnt1),mod1-2,mod1)%mod1
            h1 %= mod1
            pow2 = pow(b,(n-i)*mod2,mod2)
            pows2 = pow(pownt2,st[i],mod2)
            h2 += ti*pow2*(pows2-1)*pow(pows2*(1-invnt2),mod2-2,mod2)%mod2
            h2 %= mod2
        k1 = 0
        k2 = 0
        for i in range(ns):
            if not ss[i]:
                break
            si = s[i]
            pow1 = pow(b,(n-i)*mod1,mod1)
            pows1 = pow(powns1,ss[i],mod1)
            k1 += si*pow1*(pows1-1)*pow(pows1*(1-invns1),mod1-2,mod1)%mod1
            k1 %= mod1
            pow2 = pow(b,(n-i)*mod2,mod2)
            pows2 = pow(powns2,ss[i],mod2)
            k2 += si*pow2*(pows2-1)*pow(pows2*(1-invns2),mod2-2,mod2)%mod2
            k2 %= mod2
        k = 0
        for j in range(rs,ns+rs):
            if (h1,h2) == (k1,k2):
                l = m
                break
            i = j%ns
            si = s[i]
            sk = s[k]
            k1 -= sk*p1%mod1
            k1 += si
            k1 *= b
            k1 %= mod1
            k2 -= sk*p2%mod2
            k2 += si
            k2 *= b
            k2 %= mod2
            k += 1
        else:
            r = m
    if l == ns+1:
        print(-1)
    else:
        print(l)
    return
if __name__ == "__main__":
    solve()