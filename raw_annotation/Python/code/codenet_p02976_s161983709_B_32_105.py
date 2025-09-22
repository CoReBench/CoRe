from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline())[:-1]
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
def A():
    n = I()
    a = LI()
    ans = 0
    for i in a:
        ans ^= i
    if not ans:
        print("Yes")
    else:
        print("No")
    return
def B():
    n,m = LI()
    v = []
    for _ in range(n):
        v.append([])
    f = [0]*n
    dic = defaultdict(lambda : 0)
    for i in range(m):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
        f[a] += 1
        f[b] += 1
        dic[(a,b)] = 1
        dic[(b,a)] = 1
    ans = []
    d = [0]*n
    q = deque([0])
    bfs = [1]*n
    bfs[0] = 0
    while q:
        x = q.popleft()
        s = []
        for y in v[x]:
            if dic[(x,y)]:
                s.append(y)
            if bfs[y]:
                q.append(y)
                bfs[y] = 0
        if s:
            if len(s)%2:
                if d[x]:
                    for y in s:
                        ans.append((x,y))
                        dic[(x,y)] = 0
                        dic[(y,x)] = 0
                    d[x] = 0
                else:
                    for y in s[:-1]:
                        ans.append((x,y))
                        dic[(x,y)] = 0
                        dic[(y,x)] = 0
                    d[x] = 0
                    y = s[-1]
                    d[y] ^= 1
                    ans.append((y,x))
                    dic[(x,y)] = 0
                    dic[(y,x)] = 0
            else:
                if not d[x]:
                    for y in s:
                        ans.append((x,y))
                        dic[(x,y)] = 0
                        dic[(y,x)] = 0
                    d[x] = 0
                else:
                    for y in s[:-1]:
                        ans.append((x,y))
                        dic[(x,y)] = 0
                        dic[(y,x)] = 0
                    d[x] = 0
                    y = s[-1]
                    d[y] ^= 1
                    ans.append((y,x))
                    dic[(x,y)] = 0
                    dic[(y,x)] = 0
    if sum(d):
        print(-1)
    else:
        for i,j in ans:
            print(i+1,j+1)
    return
def C():
    n = I()
    p = [(1<<i) for i in range(100)]
    if n in p:
        print("No")
        quit()
    if n+1 in p:
        print("Yes")
        for i in range(1,2*n):
            print(i,i+1)
        quit()
    ans = []
    for i in range(1,3):
        ans.append((i,i+1))
    ans.append((3,n+1))
    for i in range(1,3):
        ans.append((i+n,i+n+1))
    u = 1
    d = 1
    for i in range(2,n//2+n%2):
        ans.append((u,2*i))
        ans.append((d,2*i+1))
        ans.append((2*i,2*i+n+1))
        ans.append((2*i+1,2*i+n))
        u = 2*i+n+1
        d = 2*i+n
    if n%2:
        print("Yes")
        for i,j in ans:
            print(i,j)
    else:
        ans.append((n-1,n))
        for i in range(n):
            if p[i]&n:
                break
        ans.append((p[i+1]-2,2*n))
        print("Yes")
        for i,j in ans:
            print(i,j)
    return
def D():
    n = I()
    return
def E():
    n = I()
    return
def F():
    n = I()
    return
if __name__ == "__main__":
    B()