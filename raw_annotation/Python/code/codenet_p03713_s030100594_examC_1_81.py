def examC(inf):
    L = LI()
    ans = inf
    for i in range(4):
        if i==0:
            for j in range(2):
                ansC = []
                if j==0:
                    cut = L[0] // 3
                    ansC.append(L[1] * cut)
                    L2 = [ L[0] - cut,L[1]]
                    cut = L2[0] // 2
                    ansC.append(L2[1] * cut)
                    ansC.append(L[1]*L[0] - sum(ansC))
                    ans = min(ans, max(ansC) - min(ansC))
                else:
                    cut = L[0] // 3+1
                    ansC.append(L[1] * cut)
                    L2 = [ L[0] - cut,L[1]]
                    cut = L2[0] // 2
                    ansC.append(L2[1] * cut)
                    ansC.append(L[1]*L[0] - sum(ansC))
                    ans = min(ans, max(ansC) - min(ansC))
        elif i==1:
            for j in range(2):
                ansC = []
                if j==0:
                    cut = L[0] // 3
                    ansC.append(L[1] * cut)
                    L2 = [ L[0] - cut,L[1]]
                    cut = L2[1] // 2
                    ansC.append(L2[0] * cut)
                    ansC.append(L[1]*L[0] - sum(ansC))
                    ans = min(ans, max(ansC) - min(ansC))
                else:
                    cut = L[0] // 3+1
                    ansC.append(L[1] * cut)
                    L2 = [ L[0] - cut,L[1]]
                    cut = L2[1] // 2
                    ansC.append(L2[0] * cut)
                    ansC.append(L[1]*L[0] - sum(ansC))
                    ans = min(ans, max(ansC) - min(ansC))
        elif i==2:
            for j in range(2):
                ansC = []
                if j==0:
                    cut = L[1] // 3
                    ansC.append(L[0] * cut)
                    L2 = [ L[0],L[1]-cut]
                    cut = L2[0] // 2
                    ansC.append(L2[1] * cut)
                    ansC.append(L[1]*L[0] - sum(ansC))
                    ans = min(ans, max(ansC) - min(ansC))
                else:
                    cut = L[1] // 3+1
                    ansC.append(L[0] * cut)
                    L2 = [ L[0],L[1]-cut]
                    cut = L2[0] // 2
                    ansC.append(L2[1] * cut)
                    ansC.append(L[1]*L[0] - sum(ansC))
                    ans = min(ans, max(ansC) - min(ansC))
        else:
            for j in range(2):
                ansC = []
                if j==0:
                    cut = L[1] // 3
                    ansC.append(L[0] * cut)
                    L2 = [ L[0],L[1]-cut]
                    cut = L2[1] // 2
                    ansC.append(L2[0] * cut)
                    ansC.append(L[1]*L[0] - sum(ansC))
                    ans = min(ans, max(ansC) - min(ansC))
                else:
                    cut = L[1] // 3+1
                    ansC.append(L[0] * cut)
                    L2 = [ L[0],L[1]-cut]
                    cut = L2[1] // 2
                    ansC.append(L2[0] * cut)
                    ansC.append(L[1]*L[0] - sum(ansC))
                    ans = min(ans, max(ansC) - min(ansC))
    print(ans)
import sys
import copy
import bisect
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')
examC(inf)