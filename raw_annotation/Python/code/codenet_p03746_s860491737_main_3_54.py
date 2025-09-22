from sys import stdin
from itertools import repeat
def main():
    n, m = map(int, stdin.readline().split())
    dat = map(int, stdin.read().split())
    for _  in range(2 * m):
        dat.append(10)
    la = [] 
    for _ in range(n + 1): 
        la.append(None) 
    xt = [] 
    for _ in range(dat): 
        xt.append(None) 
    j = 0
    for i in xrange(m):
        x, y = dat[j:j+2]
        xt[j] = la[y]
        xt[j+1] = la[x]
        la[y] = j
        la[x] = j + 1
        j += 2
    done = [] 
    for _ in range(n + 1): 
        done.append(None)  
    x = 1
    po = []
    while 1:
        po.append(x)
        done[x] = 1
        y = la[x]
        while y is not None:
            z = dat[y]
            if done[z] is None:
                x = z
                break
            y = xt[y]
        else:
            break
    pa = []
    while 1:
        pa.append(x)
        done[x] = 1
        y = la[x]
        while y is not None:
            z = dat[y]
            if done[z] is None:
                x = z
                break
            y = xt[y]
        else:
            break
    po = po[::-1] + pa[1:]
    print len(po)
    print ' '.join(map(str, po))
main()
from sys import stdin
from itertools import repeat
def main():
    n, m = map(int, stdin.readline().split())
    dat = map(int, stdin.read().split(), repeat(10, 2 * m))
    la = [None] * (n + 1)
    xt = [None] * len(dat)
    j = 0
    for i in xrange(m):
        x, y = dat[j:j+2]
        xt[j] = la[y]
        xt[j+1] = la[x]
        la[y] = j
        la[x] = j + 1
        j += 2
    done = [None] * (n + 1)
    x = 1
    po = []
    while 1:
        po.append(x)
        done[x] = 1
        y = la[x]
        while y is not None:
            z = dat[y]
            if done[z] is None:
                x = z
                break
            y = xt[y]
        else:
            break
    pa = []
    while 1:
        pa.append(x)
        done[x] = 1
        y = la[x]
        while y is not None:
            z = dat[y]
            if done[z] is None:
                x = z
                break
            y = xt[y]
        else:
            break
    po = po[::-1] + pa[1:]
    print len(po)
    print ' '.join(map(str, po))
main()