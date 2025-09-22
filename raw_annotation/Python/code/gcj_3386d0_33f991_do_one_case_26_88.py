import sys, math, os
from fractions import Fraction, gcd
LocaL = "MATE_DESKTOP_SESSION_ID" in os.environ
def mle_assert(x):
    if LocaL:
        assert x
    elif not x:
        x = range(10**8)
def tle_assert(x):
    if LocaL:
        assert x
    elif not x:
        for i in range(10000):
            for j in range(1000):
                for k in range(1000):
                    pass
sys.setrecursionlimit(10000)
ssr = sys.stdin.readline
ssw = sys.stdout.write
ssf = sys.stdout.flush
sew = sys.stderr.write
def rdline(): return ssr().strip()
def rdstrs(): return ssr().split()
def rdints(): return map(int, ssr().split())
def rd1int(): return int(rdline())
def do_one_case(cnum):
    N = rd1int()
    XY = []
    for i in range(N):
        x, y = rdints()
        XY.append((x,y))
    XY.sort()
    A = {}
    for j in xrange(1,N):
        x2, y2 = XY[j]
        for i in xrange(j):
            x1, y1 = XY[i]
            a = x2-x1
            b = y2-y1
            g = gcd(a,b)
            a /= g
            b /= g
            if (a,b) in A:
                A[(a,b)].append((i,j))
                A[(-a,-b)].append((j,i))
            else:
                A[(a,b)] = [ (i,j) ]
                A[(-a,-b)] = [ (j,i) ]
    m = 1
    for a,b in A:
        E = A[(a,b)]
        I = {}
        O = {}
        for i,j in E:
            if i in O:
                O[i].append(j)
            else:
                O[i] = [j]
            if j in I:
                I[j].append(i)
            else:
                I[j] = [i]
        NI = set(range(N)) - set(I)
        C = []
        for x in NI:
            if x in O:
                Q = [ (0,x)] + [(len(I[y]),y) for y in O[x] ]
                Q.sort()
                C.append([y for x,y in Q])
            else:
                C.append([x])
        C1 = [ q for q in C if len(q)==1 ]
        C2 = [ q for q in C if len(q)&1==0 ]
        C3 = [ q for q in C if len(q)>1 and len(q)&1==1 ]
        while len(C3)>1:
            C2.append(C3[-2]+C3[-1])
            del C3[-2:]
        C3 = (C3 + C1)[:2]
        l2 = sum(len(q) for q in C2)
        l3 = sum(len(q) for q in C3)
        if l3:
            l = l2 + l3
        elif len(C2)>1:
            l = l2-1
        else:
            l = l2
        m = max(m, l)
    print "Case #%d: %d" % (cnum, m)
def main():
    T = rd1int()
    for i in range(T):
        do_one_case(i+1)
        sys.stdout.flush()
if __name__ == "__main__":
    main()