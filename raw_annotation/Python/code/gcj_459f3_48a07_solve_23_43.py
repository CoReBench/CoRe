import sys, math
def debug(*arg):
    if False:
        print(arg)
def write(s):
    print(s)
    sys.stdout.flush()
def read():
    v = raw_input()
    return v
def readi():
    return int(raw_input())
def readia():
    return map(int, raw_input().split(" "))
def cntForOne(r,st=0):
    i = st
    cnt = 0
    while r > i:
        cnt += 1
        i += 1
        r -= i
    return cnt
def solve():
    R,B = readia()
    r = max(R,B)
    b = min(R,B)
    if b == 0:
        return cntForOne(r)
    i = 0 
    cnt = 0
    cR, cB = 0, 1
    while True:
        s = bin(i)[2:]
        cR, cB = s.count("1"), s.count("0")
        if cR > r or cB > b:
            break
        r -= cR 
        b -= cB
        i += 1
        cnt += 1
    remaining_bits = len(bits) - 1
    cnt += cntForOne(r, remaining_bits)
    return cnt
if __name__ == '__main__':
    t = readi()
    for i in range(t):
        res = solve()
        write("Case #%i: %i" % (i+1, res))