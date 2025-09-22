import math
import sys
DEBUG = False
def inp():
    return sys.stdin.readline().rstrip()
def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)
def solve(N, A):
    allxor = 0
    for a in A:
        allxor ^= a
    B = [0] * N
    ans = 0
    bcount = 0
    for bit in range(61, -1, -1):
        mask = 1 << bit
        if allxor & mask:
            ans <<= 1
            ans |= 1
            continue
        bset = set()
        for i in range(N):
            b = B[i]
            b <<= 1
            b |= (A[i] & mask) >> bit
            B[i] = b
            bset.add(b)
        bcount += 1
        full_bit = (1 << bcount) - 1
        blist = list(bset)
        blist1 = blist[:len(blist) // 2]
        blist2 = blist[len(blist) // 2:]
        r1 = set([0])
        for b in blist1:
            for c in list(r1):
                r1.add(b ^ c)
        r2 = set([0])
        for b in blist2:
            for c in list(r2):
                r2.add(b ^ c)
        best = full_bit - 1
        for b1 in r1:
            if b1 ^ full_bit in r2:
                best = full_bit
                break
        bestb = best & 1
        ans <<= 1
        ans |= bestb
        if bestb == 0:
            for i in range(N):
                B[i] >>= 1
            bcount -= 1
    return ans + (ans ^ allxor)
def main():
    N = int(inp())
    A = [int(e) for e in inp().split()]
    print(solve(N, A))
if __name__ == '__main__':
    main()