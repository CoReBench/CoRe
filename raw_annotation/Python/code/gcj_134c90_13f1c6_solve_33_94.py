from math import sqrt, pow, log, ceil, log10
from sys import stdin, setrecursionlimit
from sets import Set
setrecursionlimit(100000)
debug = False
def isCycleCorrect(A, C, L, ans):
    la = len(ans)
    for i in range(A):
        pos = 0
        isThereAWinner = False
        while (isThereAWinner == False) and (pos < L[i] * la):
            if C[i][pos % L[i]] != ans[pos % la]:
                if debug:
                    print "->", C[i][pos % L[i]], ans[pos % la], A, i
                if (C[i][pos % L[i]], ans[pos % la]) == ('R', 'S'):
                    return False
                if (C[i][pos % L[i]], ans[pos % la]) == ('S', 'R'):
                    isThereAWinner = True
                    break
                if (C[i][pos % L[i]], ans[pos % la]) == ('R', 'P'):
                    isThereAWinner = True
                    break
                if (C[i][pos % L[i]], ans[pos % la]) == ('P', 'R'):
                    return False
                if (C[i][pos % L[i]], ans[pos % la]) == ('P', 'S'):
                    isThereAWinner = True
                    break
                if (C[i][pos % L[i]], ans[pos % la]) == ('S', 'P'):
                    return False
            pos += 1
        return False
    return True
def solve(A, C, L):
    ans = ""
    pos = 0
    isAlive = [True] * A
    while True:
        possibilities = {}
        possibilities['R'] = 0
        possibilities['S'] = 0
        possibilities['P'] = 0
        predR = []
        predS = []
        predP = []
        if debug:
            print "alive ans", isAlive, ans
        if not any(isAlive):
            print ans
            return
        for i in range(A):
            if isAlive[i]:
                possibilities[C[i][pos % L[i]]] = 1
                if C[i][pos % L[i]] == 'R':
                    predR += [i]
                if C[i][pos % L[i]] == 'S':
                    predS += [i]
                if C[i][pos % L[i]] == 'P':
                    predP += [i]
                if possibilities['R'] + possibilities['S'] + possibilities['P'] == 3:
                    print "IMPOSSIBLE"
                    return
        (r, s, p) = (possibilities['R'], possibilities['S'], possibilities['P'])
        if debug:
            print "->", (r, s, p)
        if (r, s, p) == (1, 0, 0):
            ans += "P"
            print ans
            return
        if (r, s, p) == (0, 1, 0):
            ans += "R"
            print ans
            return
        if (r, s, p) == (0, 0, 1):
            ans += "S"
            print ans
            return
        if len(ans) == 500:
            print "IMPOSSIBLE"
            if debug:
                print "LEN", ans
            return
        if (r, s, p) == (1, 1, 0):
            for i in predS:
                isAlive[i] = False
            ans += "R"
        if (r, s, p) == (1, 0, 1):
            for i in predR:
                isAlive[i] = False
            ans += "P"
        if (r, s, p) == (0, 1, 1):
            for i in predP:
                isAlive[i] = False
            ans += "S"
        pos += 1
T = int(stdin.readline())
for i in range(1,T+1):
    A = stdin.readline()
    A = int(A)
    C = [""] * A
    L = [0] * A
    for j in range(A):
        C[j] = stdin.readline().rstrip() 
        L[j] = len(C[j])
    print "Case #" + str(i) + ":", 
    if debug:
        print " -> ", A, C, L
    solve(A, C, L)