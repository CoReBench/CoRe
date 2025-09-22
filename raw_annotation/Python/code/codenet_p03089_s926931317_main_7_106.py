import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    b = LI()
    ans_lst = []
    while len(b)!=0:
        lst = collections.deque([])
        mx = 1
        phase = False
        while len(b)!=0:
            nxt = b.pop()
            mx = max(mx, nxt)
            if mx==1:
                lst.appendleft(nxt)
            else:
                phase |= nxt == 1
                if phase and nxt != 1:
                    b.append(nxt)
                    break
                else:
                    lst.appendleft(nxt)
        ctn = True
        up = True
        now_mx = 0
        now_mn = mx
        lenth = 0
        for x in lst:
            if up:
                if x>=now_mx:
                    if x==mx:
                        up = False
                    else:
                        lenth += 1
                else:
                    ctn = False
                    break
            else:
                if x<=now_mn:
                    now_mn = min(now_mn, x)
                else:
                    ctn = False
                    break
        if not ctn or lenth+1<mx or lst[0] != 1:
            print(-1)
            exit(0)
        gr = [[k,len(list(g))] for k, g in itertools.groupby(lst)]
        com = len(lst)
        phase = False
        down = False
        now_len = 0
        i = 0
        while com!= 0:
            nxt = lst[-1]
            if not phase:
                if now_len+1 < nxt:
                    if not down:
                        if gr[i][0] == mx:
                            down = True
                            i -= 1
                        else:
                            ans_lst.append(gr[i][0])
                            now_len += 1
                            com -= 1
                            gr[i][1] -= 1
                            i += 1
                    else:
                        if gr[i][1] == 0:
                            i -= 1
                        else:
                            ans_lst.append(gr[i][0])
                            now_len += 1
                            com -= 1
                            gr[i][1] -= 1
                else:
                    ans_lst.append(nxt)
                    com -= 1
                    lst.pop()
                    phase |= nxt == mx
            else:
                if nxt == mx:
                    ans_lst.append(nxt)
                    com -= 1
                    lst.pop()
                else:
                    if not down:
                        if gr[i][0] == mx:
                            down = True
                            i -= 1
                        else:
                            ans_lst.append(gr[i][0])
                            com -= 1
                            gr[i][1] -= 1
                            i += 1
                    else:
                        if gr[i][1] == 0:
                            i -= 1
                        else:
                            ans_lst.append(gr[i][0])
                            com -= 1
                            gr[i][1] -= 1
    print(*ans_lst, sep="\n")
main()