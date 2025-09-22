import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
mod = 10**9+7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def main():
    n,s = LI()
    a = [LI() for _ in range(n)]
    x = [_[0] for _ in a]
    p = [_[1] for _ in a]
    if x[0] > s:
        return x[-1] - s
    if x[-1] < s:
        return s - x[0]
    r = 0
    i = 0
    j = n - 1
    d = p[:]
    e = collections.defaultdict(list)
    sk = set()
    while i < j:
        if x[i] > s:
            break
        if x[j] < s:
            break
        if d[i] >= d[j]:
            d[i] += d[j]
            j -= 1
            if j >= 0 and d[j] < d[j+1]:
                d[j] = d[j+1]
                sk.add(i)
        else:
            d[j] += d[i]
            i += 1
            if i < n and d[i] < d[i-1]:
                d[i] = d[i-1]
                sk.add(i)
    t = s
    if i == j:
        r += abs(x[i]-s)
        t = x[i]
        i -= 1
        j += 1
    else:
        if x[i] > s:
            r += abs(x[j]-s)
            t = x[j]
            i -= 1
            j += 1
        else:
            r += abs(x[i]-s)
            t = x[i]
            i -= 1
            j += 1
    while i >= 0 or j < n:
        if i < 0:
            r += abs(x[-1]-t)
            break
        if j >= n:
            r += abs(x[0]-t)
            break
        if i in sk:
            d[i-1] = d[i]
            i-=1
            continue
        if j in sk:
            d[j+1] = d[j]
            j+=1
            continue
        if d[i] >= d[j]:
            r += abs(x[i]-t)
            t = x[i]
            i -= 1
        else:
            r += abs(x[j]-t)
            t = x[j]
            j += 1
    return r
print(main())