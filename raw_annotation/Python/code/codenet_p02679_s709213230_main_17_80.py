import sys, bisect, math, itertools, string, queue, copy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations, combinations_with_replacement
from heapq import heappop, heappush
from fractions import gcd
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
def main():
    n = int(input())
    dic = defaultdict(int)
    dic1 = defaultdict(int)
    for _ in range(n):
        a,b = inpm()
        if a != 0 and b == 0:
            a = 1
        elif a == 0 and b != 0:
            b = 1
        else:
            if not (a==0 and b==0):
                m = gcd(a,b)
                a //= m
                b //= m
        if a < 0 and b < 0:
            a = -a
            b = -b
        if a < 0 and b > 0:
            a = -a
            b = -b
        index = ' '.join([str(a),str(b)])
        dic[index] += 1
        dic1[index] += 1
    ans = 1
    dic2 = defaultdict(int)
    for e in dic:
        a,b = map(int,e.split())
        if a == 0 or b == 0:
            continue
        flag = 0
        if a > 0 and b > 0:
            rev = ' '.join([str(b),str(-a)])
        else:
            rev = ' '.join([str(-b),str(a)])
        if dic1[rev] > 0 and dic2[rev] == 0:
            dic2[rev] = 1
            dic2[e] = 1
            flag = 1
        if flag:
            continue
        n1 = pow(2,dic[e],mod)
        n2 = pow(2,dic1[rev],mod)
        if n1 == 0:
            ans *= n2
        elif n2 == 0:
            ans *= n1
        else:
            ans *= (n1+n2-1)
        ans %= mod
    num = 0
    if dic['1 0'] and dic['0 1']:
        num = (pow(2,dic['1 0'],mod)+pow(2,dic['0 1'],mod)-1)
        num %= mod
    elif dic['1 0']:
        num = pow(2,dic['1 0'],mod)
        num %= mod
    elif dic['0 1']:
        num = pow(2,dic['0 1'],mod)
        num %= mod
    if num != 0:
        ans *= num
        ans %= mod
    print(ans-1+dic['0 0'])
if __name__ == "__main__":
    main()