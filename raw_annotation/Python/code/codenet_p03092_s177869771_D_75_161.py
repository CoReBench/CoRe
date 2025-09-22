from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = SR()
    return l
mod = 1000000007
sys.setrecursionlimit(1000000)
def A():
    n = I()
    b = LI()
    ans = []
    d = max(b)
    i = 0
    while b:
        j = len(b)-1
        while j >= 0:
            if b[j] > j+1:
                print(-1)
                quit()
            elif b[j] == j+1:
                ans.append(b[j])
                b.pop(j)
                break
            j -= 1
    for i in ans[::-1]:
        print(i)
def B():
    n = I()
    if n%2:
        ans = []
        for i in range(1,n+1):
            for j in range(1,n+1):
                if j != n-i and j != i:
                    ans.append((min(i,j),max(i,j)))
        ans = list(set(ans))
        print(len(ans))
        ans.sort()
        for i in ans:
            print(*i)
    else:
        ans = []
        for i in range(1,n+1):
            for j in range(1,n+1):
                if j != n+1-i and j != i:
                    ans.append((min(i,j),max(i,j)))
        ans = list(set(ans))
        print(len(ans))
        ans.sort()
        for i in ans:
            print(*i)
def C():
    return
def D():
    n,a,b = LI()
    pf = LI()
    f_ans = float("inf")
    l = []
    for i in range(n):
        l.append(pf[i])
    l.sort()
    f = defaultdict(int)
    for i in pf:
        f[i] = l.index(i)
    for c in range(2):
        p = pf.copy()
        ans = 0
        while l != p:
            d = []
            i = 0
            while i < n:
                j = i
                while j < n-1:
                    if f[p[j+1]] != f[p[j]]+1:
                        break
                    j += 1
                d.append(p[i:j+1])
                i = j+1
            m = len(d)
            ld = []
            for i in range(m):
                ld.append(d[i])
            ld.sort()
            fd = defaultdict(int)
            for i in d:
                fd[str(i)] = ld.index(i)
            if c == 0:
                for i in range(m)[::-1]:
                    if d[i] != ld[i]:
                        j = fd[str(d[i])]
                        x = d[i]
                        if j > i:
                            k = 0
                            for o in range(i+1,j+1):
                                k += len(d[o])
                            p = len(d[i])
                            ans += min(b*k,a*p)
                            d.pop(i)
                            d.insert(j,x)
                            break
                        else:
                            k = 0
                            for o in range(j,i):
                                k += len(d[o])
                            p = len(d[i])
                            ans += min(a*k,b*p)
                            d.pop(i)
                            d.insert(j,x)
                            break
            else:
                for i in range(m)[::-1]:
                    if d[i] != ld[i]:
                        j = fd[str(d[i])]
                        x = d[i]
                        if j > i:
                            k = 0
                            for o in range(i+1,j+1):
                                k += len(d[o])
                            p = len(d[i])
                            ans += min(b*k,a*p)
                            d.pop(i)
                            d.insert(j,x)
                            break
                        else:
                            k = 0
                            for o in range(j,i):
                                k += len(d[o])
                            p = len(d[i])
                            ans += min(a*k,b*p)
                            d.pop(i)
                            d.insert(j,x)
                            break
            p = [None for i in range(n)]
            s = 0
            for i in range(len(d)):
                for j in range(len(d[i])):
                    p[s+j] = d[i][j]
                s += len(d[i])
        f_ans = min(f_ans,ans)
    print(f_ans)
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