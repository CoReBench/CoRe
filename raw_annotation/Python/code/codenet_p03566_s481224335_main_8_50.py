import sys
sys.setrecursionlimit(10**9)
def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))
INF=10**20
def main():
    N=ii()
    T = list(mi())
    V = list(mi())
    if N == 1:
        t,v =T[0],V[0]
        ans = (t-v)*v
        if ans < 0:
            ans = t**2/4
        print(ans)
        exit()
    acce_areas = 0
    pre_v = 0
    for i in range(N):
        v = V[i]
        acce_areas += (v+pre_v) * abs(v-pre_v) / 2
        pre_v = v
    V.append(0)
    T.append(0)
    pre_v = 0
    rect_sums = 0
    for i in range(N):
        v,t = V[i],T[i]
        next_v = V[i+1]
        dv1 = abs(v - pre_v)
        dv2 = abs(next_v - v)
        lu = pre_v < v
        ld = not lu
        ru = v < next_v
        rd = not ru
        bottom = 0
        if lu and rd:
            bottom += t-(dv1+dv2)
        if ld and ru:
            bottom += t
        if lu and ru:
            bottom += t-dv1
        if ld and rd:
            bottom += t-dv2
        rect_sums += bottom * v
        pre_v = v
    ans = acce_areas + rect_sums + V[-2] ** 2 / 2
    print(ans)
if __name__ == "__main__":
    main()