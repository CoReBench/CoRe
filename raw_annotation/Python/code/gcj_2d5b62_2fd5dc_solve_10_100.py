def areInConflict(x, y):
    bx = "{0:b}".format(x)[::-1]
    by = "{0:b}".format(y)[::-1]
    lx = len(bx)
    ly = len(by)
    for i in range(min(lx, ly)):
        if bx[i]=="1" and by[i]=="1":
            return True
    return False
def solve(x,y):
    origX = x
    origY = y
    x = max(x, -x)
    y = max(y, -y)
    if x%2==y%2:
        return "IMPOSSIBLE"
    x1 = 1
    while x1 < x:
        x1 *= 2
    x2 = x1 - x
    y1 = 1
    while y1 < y:
        y1 *= 2
    y2 = y1 - y
    if not areInConflict(x, y):
        bx = "{0:b}".format(x)[::-1]
        by = "{0:b}".format(y)[::-1]
        result = [None] * max(len(bx),len(by))
        for i in range(len(bx)):
            if bx[i] == "1":
                result[i] = "E"
        for i in range(len(by)):
            if by[i] == "1":
                result[i] = "N"
    elif not areInConflict(x2, x1) and not areInConflict(x2, y) and not areInConflict(x1, y):
        bx1 = "{0:b}".format(x1)[::-1]
        bx2 = "{0:b}".format(x2)[::-1]
        by = "{0:b}".format(y)[::-1]
        result = [None] * max(len(bx1), len(bx2), len(by))
        for i in range(len(bx1)):
            if bx1[i] == "1":
                result[i] = "E"
        for i in range(len(bx2)):
            if bx2[i] == "1":
                result[i] = "W"
        for i in range(len(by)):
            if by[i] == "1":
                result[i] = "N"
    elif not areInConflict(y2, y1) and not areInConflict(y2, x) and not areInConflict(y1, x):
        by1 = "{0:b}".format(y1)[::-1]
        by2 = "{0:b}".format(y2)[::-1]
        bx = "{0:b}".format(x)[::-1]
        result = [None] * max(len(by1), len(by2), len(bx))
        for i in range(len(bx)):
            if bx[i] == "1":
                result[i] = "E"
        for i in range(len(by1)):
            if by1[i] == "1":
                result[i] = "N"
        for i in range(len(by2)):
            if by2[i] == "1":
                result[i] = "S"
    elif not areInConflict(y2, y1) \
        and not areInConflict(y2, x1) \
        and not areInConflict(y2, x2) \
        and not areInConflict(y1, x1) \
        and not areInConflict(y1, x2) \
        and not areInConflict(x2, x1):
        bx1 = "{0:b}".format(x1)[::-1]
        bx2 = "{0:b}".format(x2)[::-1]
        by1 = "{0:b}".format(y1)[::-1]
        by2 = "{0:b}".format(y2)[::-1]
        result = [None] * max(len(by1), len(by2), len(bx))
        for i in range(len(bx1)):
            if bx1[i] == "1":
                result[i] = "E"
        for i in range(len(bx2)):
            if bx2[i] == "1":
                result[i] = "W"
        for i in range(len(by1)):
            if by1[i] == "1":
                result[i] = "N"
        for i in range(len(by2)):
            if by2[i] == "1":
                result[i] = "S"
    else:
        return "IMPOSSIBLE"
    if x != origX:
        for i in xrange(len(result)):
            if result[i]=="W":
                result[i] = "E"
            elif result[i]=="E":
                result[i] = "W"
    if y != origY:
        for i in xrange(len(result)):
            if result[i]=="N":
                result[i] = "S"
            elif result[i]=="S":
                result[i] = "N"
    return "".join(result)
T = int(raw_input())
for t in range(T):
    x,y = map(int,raw_input().split())
    print "Case #{}: {}".format(t+1, solve(x, y))