import sys
def solve(R, C):
    moves = []
    if R > C:
        flippedmoves = solve(C, R)
        for move in flippedmoves:
            moves.append((move[1], move[0]))
        return moves
    if R == 2 and C == 2:
        return moves
    if R == 2 and C == 3:
        return moves
    if R == 2 and C == 4:
        return moves
    if R == 3 and C == 3:
        return moves
    if R == 3 and C == 4:
        moves.append((1, 1))
        moves.append((2, 3))
        moves.append((3, 1))
        moves.append((2, 4))
        moves.append((1, 2))
        moves.append((3, 3))
        moves.append((1, 4))
        moves.append((2, 2))
        moves.append((3, 4))
        moves.append((2, 1))
        moves.append((1, 3))
        moves.append((3, 2))
        return moves
    if R == 4 and C == 4:
        moves.append((1, 1))
        moves.append((2, 3))
        moves.append((3, 1))
        moves.append((4, 3))
        moves.append((2, 4))
        moves.append((1, 2))
        moves.append((3, 3))
        moves.append((1, 4))
        moves.append((2, 2))
        moves.append((4, 1))
        moves.append((3, 4))
        moves.append((2, 1))
        moves.append((4, 2))
        moves.append((1, 3))
        moves.append((4, 4))
        moves.append((3, 2))
        return moves
    if R == 2:
        for c in range(3, C+1):
            moves.append((2, c))
            moves.append((1, c-2))
        if C != 6:
            moves.append((2, 1))
            moves.append((1, C-1))
            moves.append((2, 2))
            moves.append((1, C))
        else:
            moves.append((2, 1))
            moves.append((1, C))
            moves.append((2, 2))
            moves.append((1, C-1))
        return moves
    if R == 3:
        for c in range(3, C+1):
            moves.append((2, c))
            moves.append((1, c-2))
            moves.append((3, c-1))
        moves.append((2, 1))
        moves.append((3, C))
        moves.append((1, C-1))
        moves.append((2, 2))
        moves.append((1, C))
        moves.append((3, 1))
        return moves
    prevmoves = solve(R-2, C)
    for c in range(3, C+1):
        moves.append((2, c))
        moves.append((1, c-2))
    if C != 6:
        moves.append((2, 1))
        moves.append((1, C-1))
        moves.append((2, 2))
        moves.append((1, C))
    else:
        moves.append((2, 1))
        moves.append((1, C))
        moves.append((2, 2))
        moves.append((1, C-1))
    for move in prevmoves:
        moves.append((move[0]+2, move[1]))
    return moves
def invalid(pt1, pt2):
    if pt1[0] == pt2[0]:
        return True
    if pt1[1] == pt2[1]:
        return True
    if pt1[0] - pt1[1] == pt2[0] - pt2[1]:
        return True
    if pt1[0] + pt1[1] == pt2[0] + pt2[1]:
        return True
    return False
T = int(raw_input())
for i in range(T):
    stuff = [int(j) for j in raw_input().split()]
    R = stuff[0]
    C = stuff[1]
    moves = solve(R, C)
    if len(moves) == 0:
        print "Case #" + str(i+1) + ": IMPOSSIBLE"
    else:
        print "Case #" + str(i+1) + ": POSSIBLE"
        for move in moves:
            print str(move[0]) + ' ' + str(move[1])