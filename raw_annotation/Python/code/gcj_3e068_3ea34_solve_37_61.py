import random
import sys
cur_line = ""
def read_word():
    global cur_line
    i = cur_line.find(" ")
    if i == -1:
        ret = cur_line
        cur_line = ""
    else:
        ret = cur_line[:i]
        cur_line = cur_line[i+1:]
    return ret
def read_int():
    return int(read_word())
def read_float():
    return float(read_word())
def read_bool(true_word="t", false_word="f"):
    c = read_word()
    if c == true_word:
        return True
    if c == false_word:
        return False
    raise Exception(repr(c) + " is neither " + repr(true_word) + " nor " + repr(false_word))
def next_line():
    global cur_line
    try:
        cur_line = raw_input().strip()
    except EOFError:
        cur_line = ""
def run_solver(solve_function, out_file=sys.stdout):
    while not cur_line:
        next_line()
    t = read_int()
    for case in xrange(1, t+1):
        solve_function(case)
def solve(case_index):
    USED = 0xFFFFFFF
    next_line()
    n = read_int()
    counts = [0] * n
    for i in xrange(n):
        next_line()
        d = read_int()
        if d == 0:
            print "-1"
            continue
        cur = []
        for j in xrange(d):
            itemaa = read_int()
            cur.append(itemaa)
        random.shuffle(cur)
        for index in cur:
            if counts[index] != USED:
                counts[index] += 1
        chosen_index = min(cur, key=lambda i: counts[i])
        if counts[chosen_index] == USED:
            print "-1"
        else:
            print chosen_index
            counts[chosen_index] = USED
if __name__ == "__main__":
    if len(sys.argv) != 1:
        sys.stdin = open(sys.argv[1])
    run_solver(solve)