import sys
def printf(s):
    print >> sys.stdout, s
    sys.stdout.flush()
def get():
    r = raw_input()
    return r
def run_test(F):
    sol = ''
    missing = ['A', 'B', 'C', 'D', 'E']
    attempt_number = 0
    for i in xrange(1,5):
        exclude = ['A', 'B', 'C', 'D', 'E']
        found = {'A': 0,
                 'B': 0,
                 'C': 0,
                 'D': 0,
                 'E': 0,
                 }
        if 'A' in sol:
            found['A'] += 1
        if 'B' in sol:
            found['B'] += 1
        if 'C' in sol:
            found['C'] += 1
        if 'D' in sol:
            found['D'] += 1
        if 'E' in sol:
            found['E'] += 1
        for j in xrange(118):
            attempt_number += 1
            printf(str(5*j+i))
            r = get()
            found[r] = found[r] + 1
        if found['A'] >= 24:
            exclude.remove('A')
        if found['B'] >= 24:
            exclude.remove('B')
        if found['C'] >= 24:
            exclude.remove('C')
        if found['D'] >= 24:
            exclude.remove('D')
        if found['E'] >= 24:
            exclude.remove('E')
        if len(exclude) == 1:
            sol += exclude[0]
            missing.remove(exclude[0])
        else:
            printf(str(5 * 118 + i))
            r = get()
            exclude.remove(r)
            sol += exclude[0]
            missing.remove(exclude[0])
    return sol+missing[0]
t,F = [int(x) for x in raw_input().split()] 
for i in xrange(1, t + 1):
    sol = run_test(F)
    printf(sol)
    if raw_input() != 'Y':
        raise ValueError