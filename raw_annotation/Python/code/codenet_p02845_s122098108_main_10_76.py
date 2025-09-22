import bisect
from collections import deque
import sys
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = lambda *something : print(*something) if DEBUG else 0
DEBUG = True
def index(a,b):
    return str(min(a,b)) + "," +  str(max(a, b))
def main(given = sys.stdin.readline):
    input = lambda : given().rstrip()
    LMIIS = lambda : list(map(int,input().split()))
    II = lambda : int(input())
    XLMIIS = lambda x : [LMIIS() for _ in range(x)]
    n = II()
    a = LMIIS()
    if a[0] != 0:
        print(0)
        exit()
    if n == 1:
        if a[0] == 0:
            print(3)
        else:
            print(0)
        exit()
    elif n == 2:
        if a[1] == 0:
            print(3)
        if a[1] == 1:
            print(6)
        else:
            print(0)
        exit()
    if a[1] == 0 and a[2] == 0:
        x = 1
        y = 1
        z = 1
        res = 1
    elif a[1] == 0 and a[2] == 1:
        x = 2
        y = 1
        z = 0
        res = 2
    elif a[1] == 1 and a[2] == 2:
        x = 3
        y = 0
        z = 0
        res = 1
    else:
        print(0)
        exit()
    MOD = 10**9+7
    for i in range(3, n):
        if a[i] == x and a[i] != y:
            x += 1
        elif a[i] == x and a[i] == y and a[i] != z:
            res = res*2 % MOD
            x += 1
        elif a[i] == x and a[i] == y and a[i] == z:
            res = res*3 % MOD
            x += 1
        elif a[i] == y and a[i] != z:
            y += 1
        elif a[i] == y and a[i] == z:
            res = res*2 % MOD
            y += 1
        elif a[i] == z:
            z += 1
        else:
            print(0)
            exit()
    if y == 0:
        res = res* 3 % MOD
    else:
        res = res* 6 % MOD
    print(res)
if __name__ == '__main__':
    main()