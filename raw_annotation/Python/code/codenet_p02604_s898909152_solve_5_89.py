import sys
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def solve():
    n = I()
    p = [LI() for i in range(n)]
    p.sort()
    m = 1<<n
    s = 0
    for i,(x,y,num) in enumerate(p):
        d = min(abs(x),abs(y))
        s += num*d
    ans = [s]*(n+1)
    ans[-1] = 0
    pow = [1<<i for i in range(n)]
    dx = [[None]*m for i in range(n)]
    dy = [[None]*m for i in range(n)]
    for b in range(m):
        lx = []
        ly = []
        res = b
        for x,y,_ in p:
            j = res&1
            if j:
                lx.append(x)
                ly.append(y)
            res >>= 1
        ly.sort()
        for j,(x,y,num) in enumerate(p):
            i = bisect.bisect_left(lx,x)-1
            dxj = abs(x)
            dyj = abs(y)
            if i >= 0:
                nd = x-lx[i]
                if nd < dxj:
                    dxj = nd
            i += 1
            if i < len(lx):
                nd = lx[i]-x
                if nd < dxj:
                    dxj = nd
            i += 1
            if i < len(lx):
                nd = lx[i]-x
                if nd < dxj:
                    dxj = nd
            i = bisect.bisect_left(ly,y)-1
            if i >= 0:
                nd = y-ly[i]
                if nd < dyj:
                    dyj = nd
            i += 1
            if i < len(ly):
                nd = ly[i]-y
                if nd < dyj:
                    dyj = nd
            i += 1
            if i < len(ly):
                nd = ly[i]-y
                if nd < dyj:
                    dyj = nd
            dx[j][b] = dxj*num
            dy[j][b] = dyj*num
    m = 3**n
    for b in range(m):
        kx = ky = cnt = 0
        res = b
        for i in range(n):
            j = res%3
            if j:
                cnt += 1
                if j == 1:
                    kx |= pow[i]
                else:
                    ky |= pow[i]
            res //= 3
        s = 0
        ans_ = ans[cnt]
        for i in range(n):
            d = min(dx[i][kx],dy[i][ky])
            s += d
            if s >= ans_:
                break
        else:
            ans[cnt] = s
    for i in ans:
        print(i)
    return
if __name__ == "__main__":
    solve()