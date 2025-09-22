from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
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
    n = S()
    for i in n:
        if i == "1":
            print(9,end = "")
        else:
            print(1,end = "")
    print()
def B():
    n = I()
    for i in range(n,1000):
        if i%111 == 0:
            print(i)
            quit()
    return
def C():
    return
def D():
    n = I()
    p = []
    for i in range(n):
        p.append(LI())
    b = []
    for i in range(n):
        x,y = p[i]
        for j in range(i):
            s,t = p[j]
            if (abs(x-s)+abs(y-t))%2:
                print(-1)
                return
    ans = []
    for i in range(n):
        f = 0
        x,y = p[i]
        if not (x+y)%2:
            x -= 1
            if not ans:
                ans.append(1)
        if x < 0:
            x = -x
            f |= 1
        if y < 0:
            y = -y
            f |= 2
        bx = list(map(int, bin(x)[2:]))
        by = list(map(int, bin(y)[2:]))
        bx = bx[::-1]
        by = by[::-1]
        for _ in range(39-len(bx)):
            bx.append(0)
        for _ in range(39-len(by)):
            by.append(0)
        b.append([bx,by,f])
    for i in range(39):
        ans.append(1<<i)
    v = [[] for i in range(n)]
    for i in range(n):
        x,y,f = b[i]
        if x[0]:
            p = 1
            v[i].append(0)
        else:
            p = 0
            v[i].append(1)
        for j in range(1,39):
            if p:
                if x[j]:
                    if y[j]:
                        v[i][-1] ^= 3
                        x[j+1] = 1
                        v[i].append(1)
                        p = 0
                    else:
                        v[i].append(0)
                else:
                    if y[j]:
                        v[i].append(1)
                        p = 0
                    else:
                        v[i][-1] ^= 3
                        v[i].append(0)
            else:
                if y[j]:
                    if x[j]:
                        v[i][-1] ^= 3
                        y[j+1] ^= 1
                        v[i].append(0)
                        p = 1
                    else:
                        v[i].append(1)
                else:
                    if x[j]:
                        v[i].append(0)
                        p = 1
                    else:
                        v[i][-1] ^= 3
                        v[i].append(1)
        for j in range(39):
            if v[i][j] in [0,3]:
                if f&1:
                    v[i][j]^=3
            else:
                if f&2:
                    v[i][j]^=3
    p = ["R","U","D","L"]
    print(len(ans))
    print(*ans)
    for i in v:
        if len(ans) == 40:
            print("R",end = "")
        for j in i:
            print(p[j],end = "")
        print()
    return
def E():
    return
def F():
    return
def G():
    return
def H():
    return
if __name__ == "__main__":
    D()