from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
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
mod = 1000000007
dd = [(1,0),(-1,0),(0,1),(0,-1)]
def solve():
    h,w,k = LI()
    y,x,s,t = LI()
    D = [(k,0),(-k,0),(0,k),(0,-k)]
    y -= 1
    x -= 1
    s -= 1
    t -= 1
    q = deque([(y,x,-1,0)])
    d = [[float("inf")]*w for i in range(h)]
    d[y][x] = 0
    ri = []
    le = []
    do = []
    up = []
    c = []
    for i in range(h):
        c.append(input())
        ri.append([0] * w)
        le.append([0] * w)
        do.append([0] * w)
        up.append([0] * w)
    for i in range(h):
        ri[i][-1] = 0
        for j in range(w-1)[::-1]:
            if c[i][j+1] == "@":
                ri[i][j] = 0
            else:
                l = ri[i][j+1]
                if l < k:
                    ri[i][j] = l+1
                else:
                    ri[i][j] = k
    for i in range(h):
        le[i][0] = 0
        for j in range(1,w):
            if c[i][j-1] == "@":
                le[i][j] = 0
            else:
                l = le[i][j-1]
                if l < k:
                    le[i][j] = l+1
                else:
                    le[i][j] = k
    for j in range(w):
        do[-1][j] = 0
        for i in range(h-1)[::-1]:
            if c[i+1][j] == "@":
                do[i][j] = 0
            else:
                l = do[i+1][j]
                if l < k:
                    do[i][j] = l+1
                else:
                    do[i][j] = k
    for j in range(w):
        up[0][j] = 0
        for i in range(1,h):
            if c[i-1][j] == "@":
                up[i][j] = 0
            else:
                l = up[i-1][j]
                if l < k:
                    up[i][j] = l+1
                else:
                    up[i][j] = k
    while q:
        y,x,p,l = q.popleft()
        if (y,x) == (s,t):
            print(d[s][t])
            return
        nd = d[y][x] + 1
        for i in range(4):
            if i == 0:
                dy,dx = -up[y][x],0
            elif i == 1:
                dy,dx = do[y][x],0
            elif i == 2:
                dy,dx = 0,-le[y][x]
            else:
                dy,dx = 0,ri[y][x]
            ny,nx = y+dy,x+dx
            if (y,x) == (ny,nx):
                continue
            if nd < d[ny][nx]:
                diff = abs(ny-y)+abs(nx-x)
                d[ny][nx] = nd
                q.append((ny,nx,i,diff))
        if p >= 0 and l > 1:
            dy,dx = dd[p]
            ny,nx = y+dy,x+dx
            nd = d[y][x]
            if nd < d[ny][nx]:
                d[ny][nx] = nd
                q.appendleft((ny,nx,p,l-1))
    print(-1)
    return
if __name__ == "__main__":
    solve()