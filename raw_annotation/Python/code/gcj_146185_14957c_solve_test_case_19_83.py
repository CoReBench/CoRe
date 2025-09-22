import sys
from datetime import datetime
from random import randint
from itertools import cycle
def debug(x):
    sys.stderr.write('{} DEBUG: {}\n'.format(datetime.now().time(), x))
def read_int():
    return int(raw_input())
def read_float():
    return float(raw_input())
def read_words():
    return raw_input().split()
def read_ints():
    return map(int, read_words())
def read_floats():
    return map(float, read_words())
ALLVALS = set(range(1, 100))
OT = {19: 20, 20:19}
def solve_test_case():
    curd = 0
    while curd < 54:
        curd = read_int()
        if curd == -1:
            sys.exit()
        if curd > 36:
            token = 100
        else:
            token = randint(1, 99)
        print '{} {}'.format(1 + (curd % 18), token)
        sys.stdout.flush()
    badv = []
    while curd < 72:
        curd = read_int()
        if curd == -1:
            sys.exit()
        v = 1 + (curd % 18)
        print '{} {}'.format(v, 0)
        sys.stdout.flush()
        offset = 0
        if curd <= 63:
            offset = 1
        badv.append((len(read_ints()) + offset, v))
    badv = sorted(badv)
    while True:
        i, x = badv[0]
        curd = read_int()
        if curd == -1:
            sys.exit()
        print '{} {}'.format(x, randint(1, 99))
        badv[0] = (i+1, x)
        badv = sorted(badv)
        sys.stdout.flush()
        if curd == 95:
            break
    lv = rv = None
    choice = None
    while curd < 99:
        curd = read_int()
        if curd == -1:
            sys.exit()
        if not lv:
            print '{} {}'.format(19, 0)
            sys.stdout.flush()
            lv = set(read_ints())
            continue
        elif not rv:
            print '{} {}'.format(20, 0)
            sys.stdout.flush()
            rv = set(read_ints())
            if not choice:
                if len(lv) > len(rv):
                    choice = 19
                else:
                    choice = 20
            continue
        print '{} {}'.format(choice, randint(1, 99))
        sys.stdout.flush()
    choice = OT[choice]
    curd = read_int()
    if curd == -1:
        sys.exit()
    print '{} {}'.format(choice, 100)
    sys.stdout.flush()
def main():
    T = int(raw_input())
    for tc in xrange(1, T+1):
        solve_test_case()
if __name__ == "__main__":
    main()