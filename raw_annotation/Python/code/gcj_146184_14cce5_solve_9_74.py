import sys
import itertools
import math
import collections
import functools
sys.setrecursionlimit(10000)
def inputInts():
    return map(int, raw_input().split())
def solve(N, M):
    topHigh = None
    botHigh = None
    topLow = None
    botLow = None
    for i in xrange(N):
        for j in xrange(i+1, N):
            a = M[i][0]
            b = M[i][1]
            c = M[j][0]
            d = M[j][1]
            if a == c or b == d:
                continue
            top = a-c
            bot = d-b
            wasNeg = (top * bot < 0)
            top = abs(top)
            bot = abs(bot)
            if b-d > 0: 
                if wasNeg:
                    return None
                if topHigh is None or top * botHigh < topHigh * bot:
                    topHigh = top
                    botHigh = bot
            else: 
                if wasNeg:
                    continue
                if topLow is None or top * botHigh > topHigh * bot:
                    topLow = top
                    botLow = bot
    if topHigh is None and topLow is None:
        return [1, 1]
    if topHigh is None:
        if botLow == topLow:
            return [1, 2]
        elif topLow > botLow:
            return [1, int(math.ceil(topLow/botLow))]
        else:
            return [int(math.ceil(botLow/topLow)), 1]
    if topLow is None:
        if botHigh == topHigh:
            return [2, 1]
        elif botHigh > topHigh:
            return [int(math.ceil(botHigh/topHigh)), 1]
        else:
            return [1, int(math.ceil(topHigh/botHigh))]
    a = topHigh / float(botHigh)
    b = topLow / float(botLow)
    if a <= b:
        return None
    xMin = 1
    xMax = 1e20
    while xMax > xMin:
        mid = int((xMax + xMin) / 2.)
        low = b*mid
        high = a*mid
        if low == int(low):
            if high > low + 1:
                xMax = mid
            else:
                xMin = mid+1
        else:
            if math.ceil(low) < high:
                xMax = mid
            else:
                xMin = mid+1
T = int(raw_input())
for testId in range(T):
    N = int(raw_input())
    M = []
    for n in xrange(N):
        M.append(inputInts())
    res = solve(N, M)
    if res is None:
        print "Case #{:d}: IMPOSSIBLE".format(testId+1)
    else:
        print "Case #{:d}: {:d} {:d}".format(testId+1, res[0], res[1])