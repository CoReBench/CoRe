from __future__ import division
import math
import sys
def printflush(x):
    print(x)
    sys.stdout.flush()
def getline():
    return sys.stdin.readline().split()
def getints():
    return [int(x) for x in getline()]
def solvecase():
    vases = [None] + [[] for i in range(20)]
    peektime = [0 for i in range(21)]
    stuffV = None
    tokens = 0
    target = 1
    for d in range(1, 101):
        (dd,) = getints()
        assert(d == dd)
        tokens += 1
        if d <= 19:
            V = d
            P = 100
        elif d == 100:
            V = 20
            P = 100
        elif stuffV is not None:
            V = stuffV
            v = vases[V]
            sys.stderr.write("TARGET peektime: %s\n" % peektime[target])
            if peektime[target] <= d - 5:
                V = target
                P = 0
                sys.stderr.write("PEEK TARGET instead\n")
            elif peektime[V] <= d - 30:
                P = 0
                sys.stderr.write("PEEK instead\n")
            else:
                P = 1
                while True:
                    if P not in v:
                        break
                    P += 1
        else:
            V = target
            P = 0
        printflush("{} {}".format(V, P))
        stuffV = None
        if P == 0:
            L = getints()
            L = [x for x in L[1:] if x < 100]
            vases[V] = L
            peektime[V] = d
        elif P != 100:
            vases[V].append(P)
            tokens += 1
        m = min(len(vases[V]) for V in range(1, 21))
        sys.stderr.write("day = %s; m = %s; target = %s\n" % (d, m, target))
        sys.stderr.write("sizes: %s\n" % " ".join(str(len(vases[V])) for V in range(1, 21)))
        if len(vases[target]) == m:
            m2 = 10000
            mtime = 0
            for V in range(1, 21):
                if V == target:
                    continue
                if len(vases[V]) < m2 or (len(vases[V]) == m2 and peektime[V] > mtime):
                    stuffV = V
                    m2 = len(vases[V])
                    mtime = peektime[V]
            sys.stderr.write("STUFFING vase %s\n" % stuffV)
        else:
            for target in range(1, 21):
                if len(vases[target]) == m:
                    break
            sys.stderr.write("NEW target = %s\n" % target)
(T,) = getints()
for i in range(T):
    ans = solvecase()
    sys.stderr.write("*" * 80 + "\n")