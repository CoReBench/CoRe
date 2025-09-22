import sys,collections,itertools,re,math,fractions,decimal,random,array,bisect,heapq
def solve(f, w):
    cnt = {}
    for i in [50, 200]:
        print i
        sys.stdout.flush()
        cnt[i] = f.read_int()
    for i in xrange(w-2):
        print 1
        sys.stdout.flush()
        f.read_int()
    sys.stderr.write("%s\n"%cnt)
    c = [0] * 6
    c[5] = (cnt[200] % (2**40)) / (2**33)
    c[4] = (cnt[200] % (2**50)) / (2**40)
    c[3] = cnt[200] / (2**50)
    cnt[50] -= c[3] * 2**12 + c[4] * 2**10 + c[5] * 2**8
    c[2] = (cnt[50] % (2**25)) / (2**16)
    c[1] = (cnt[50] % (2**50)) / (2**25)
    c[0] = cnt[50] / (2**50)
    print " ".join(map(str, c))
    sys.stdout.flush()
    verdict = f.read_int()
    if verdict != 1:
        sys.exit()
class Reader(object):
    def __init__(self, filename=None):
        self.file = open(filename) if filename is not None else None
    def __readline(self):
        return self.file.next().strip() if self.file else raw_input()
    def read_int(self): return int(self.__readline())
    def read_float(self): return float(self.__readline())
    def read_long(self): return long(self.__readline())
    def read_decimal(self): return decimal.Decimal(self.__readline())
    def read_str(self): return self.__readline()
    def read_int_list(self): return map(int, self.__readline().split())
    def read_float_list(self): return map(float, self.__readline().split())
    def read_long_list(self): return map(long, self.__readline().split())
    def read_decimal_list(self): return map(decimal.Decimal, self.__readline().split())
    def read_str_list(self): return self.__readline().split()
if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    f = Reader(filename)
    cases, w = f.read_int_list()
    for case in xrange(cases):
        solve(f, w)