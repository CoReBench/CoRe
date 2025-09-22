import sys, bisect, math, itertools, string, queue, copy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])
def bfs(n,g):
    went = [False]*n
    dis = [0 for _ in range(n)]
    que = deque([])
    que.append(0)
    went[0] = True
    cnt_odd = 0
    cnt_even = 1
    while que:
        go = que.pop()
        for i in range(len(g[go])):
            if went[g[go][i]]:
                continue
            dis[g[go][i]] = dis[go] + 1
            went[g[go][i]] = True
            if dis[g[go][i]]%2 == 0:
                cnt_even += 1
            else:
                cnt_odd += 1
            que.append(g[go][i])
    return dis,cnt_odd,cnt_even
def length3(s,n,g,ans,que_1,que_2):
    went = [False]*n
    dis = [0] * n
    see = []
    que = deque([])
    que.append(s)
    went[s] = True
    while que:
        go = que.pop()
        for i in range(len(g[go])):
            if went[g[go][i]]:
                continue
            dis[g[go][i]] = dis[go] + 1
            went[g[go][i]] = True
            if dis[g[go][i]] < 3:
                que.append(g[go][i])
            elif dis[g[go][i]] == 3:
                see.append(g[go][i])
    check1 = 0
    check2 = 0
    for e in see:
        if ans[e] == 0:
            continue
        if ans[e]%3 == 1:
            check1 += 1
        if ans[e]%3 == 2:
            check2 += 1
    if check1>0 and check2>0:
        print(-1)
        exit()
    if check1>0:
        if que_2:
            ans[s] = que_2.pop()
        else:
            print(-1)
            exit()
        for e in see:
            if ans[e] == 0:
                if que_1:
                    ans[e] = que_1.pop()
                else:
                    print(-1)
                    exit()
    elif check2>0:
        if que_1:
            ans[s] = que_1.pop()
        else:
            print(-1)
            exit()
        for e in see:
            if ans[e] == 0:
                if que_2:
                    ans[e] = que_2.pop()
                else:
                    print(-1)
                    exit()
    else:
        if len(que_1) > len(que_2):
            if que_2:
                ans[s] = que_2.pop()
            else:
                print(-1)
                exit()
            for e in see:
                if ans[e] == 0:
                    if que_1:
                        ans[e] = que_1.pop()
                    else:
                        print(-1)
                        exit()
        else:
            if que_1:
                ans[s] = que_1.pop()
            else:
                print(-1)
                exit()
            for e in see:
                if ans[e] == 0:
                    if que_2:
                        ans[e] = que_2.pop()
                    else:
                        print(-1)
                        exit()
    return ans,que_1,que_2
def main():
    n = inp()
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        a,b = inpm()
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    dis,cnt_odd,cnt_even = bfs(n,g)
    ans = [0 for _ in range(n)]
    if min(cnt_even,cnt_odd) <= n//3:
        check = [1 for _ in range(n)]
        x = 1
        if cnt_even <= cnt_odd:
            for i in range(n):
                if dis[i]%2 == 0:
                    ans[i] = 3*x
                    check[3*x-1] = 0
                    x += 1
            x = 0
            for i in range(n):
                if ans[i] == 0:
                    while not check[x]:
                        x += 1
                    ans[i] = x + 1
                    x += 1
            print(*ans)
        elif cnt_even >= cnt_odd:
            for i in range(n):
                if dis[i]%2 == 1:
                    ans[i] = 3*x
                    check[3*x-1] = 0
                    x += 1
            x = 0
            for i in range(n):
                if ans[i] == 0:
                    while not check[x]:
                        x += 1
                    ans[i] = x + 1
                    x += 1
            print(*ans)
        return
    check = [1 for _ in range(n)]
    x = 1
    if cnt_even <= cnt_odd:
        remain = []
        for i in range(n):
            if dis[i]%2 == 0:
                if x*3 <= n:
                    ans[i] = 3*x
                    check[3*x-1] = 0
                    x += 1
                else:
                    remain.append(i)
        que_1 = deque()
        que_2 = deque()
        for i in range(n):
            if (i+1)%3 == 1:
                que_1.append(i+1)
            elif (i+1)%3 == 2:
                que_2.append(i+1)
        for e in remain:
            ans,que_1,que_2 = length3(e,n,g,ans,que_1,que_2)
        for i in range(n):
            if ans[i] == 0:
                if que_1:
                    ans[i] = que_1.pop()
                else:
                    ans[i] = que_2.pop()
        print(*ans)
    else:
        remain = []
        for i in range(n):
            if dis[i]%2 == 1:
                if x*3 <= n:
                    ans[i] = 3*x
                    check[3*x-1] = 0
                    x += 1
                else:
                    remain.append(i)
        que_1 = deque()
        que_2 = deque()
        for i in range(n):
            if (i+1)%3 == 1:
                que_1.append(i+1)
            elif (i+1)%3 == 2:
                que_2.append(i+1)
        for e in remain:
            ans,que_1,que_2 = length3(e,n,g,ans,que_1,que_2)
        for i in range(n):
            if ans[i] == 0:
                if que_1:
                    ans[i] = que_1.pop()
                else:
                    ans[i] = que_2.pop()
        print(*ans)
if __name__ == "__main__":
    main()