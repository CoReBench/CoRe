def ILA(s, t):
    rows = len(s)+1
    cols = len(t)+1
    dist = [[0 for x in range(cols)] for x in range(rows)]
    choice = [[0 for x in range(cols)] for x in range(rows)]
    for row in range(1, rows):
        dist[row][0] = row
        choice[row][0] = 'D'
    for col in range(1, cols):
        dist[0][col] = col
        choice[0][col] = 'I'
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                subs = 0
            else:
                subs = 1
            m = min(dist[row-1][col] + 1,
                    dist[row][col-1] + 1,
                    dist[row-1][col-1] + subs) 
            dist[row][col] = m
            if m == dist[row-1][col] + 1:
                choice[row][col] = 'D'
            elif m == dist[row][col-1] + 1:
                choice[row][col] = 'I'
            elif subs == 1:
                choice[row][col] = 'S'
            else:
                choice[row][col] = 'N'     
    time = dist[row][col]
    target = int(time/2)
    path = [None]*(time+1)
    path[0] = s
    path[time] = t
    c_s = list(s)
    c_t = list(t)
    start = 1
    end = time-1
    suffix = []
    while end >= start:
        move = choice[len(c_s)][len(c_t)]
        if move == 'D':
            del c_s[-1]
            path[start] = ''.join(c_s + suffix)
            start += 1
        elif move == 'I':
            del c_t[-1]
            path[end] = ''.join(c_t + suffix)
            end -= 1
        elif move == 'S':
            suffix = [c_t[-1]] + suffix
            del c_s[-1]
            del c_t[-1]
            path[start] = ''.join(c_s + suffix)
            start += 1
        elif move == 'N':
            suffix = [c_t[-1]] + suffix
            del c_s[-1]
            del c_t[-1]
    return path[target]
def solve_case(C, J):
    return ILA(C, J)
def main():
    T = int(raw_input())
    for case_no in xrange(1,1+T):
        C, J = raw_input().split(' ')
        ans = solve_case(C, J)
        print "Case #{}: {}".format(case_no, ans)
main()