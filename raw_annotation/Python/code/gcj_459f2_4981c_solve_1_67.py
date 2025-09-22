def solve(B):
    if B[0] == 0 or B[-1] == 0:
        return 'IMPOSSIBLE', None
    grid = []
    C = len(B)
    grid = []
    for j in range(C):
        row = []
        for i in range(C):
            row.append('.')
        grid.append(row)
    shadowed = [False] * len(C)
    shadowed[0] = True
    B[0] -= 1
    B[-1] -= 1
    i = 0
    for i in range(C):
        if B[i] == 0 and shadowed[i]:
            continue
        if B[i] > 0 and not shadowed[i]:
            unshadowed_balls = 0
            j = i - 1
            l = 1
            while j >= 1 and not shadowed[j]:
                grid[l][j] = '\\'
                shadowed[j] = True
                unshadowed_balls += 1
                l += 1
                j -= 1
            if B[i] <= unshadowed_balls:
                excess_balls = unshadowed_balls - B[i] + 1
                j = i
                while excess_balls > 1:
                    j -= 1
                    excess_balls -= 1
                    shadowed[j] = False
            else:
                B[i] -= (unshadowed_balls + 1)
                shadowed[i] = True
        if B[i] > 0 and shadowed[i]:
            r = B[i]
            j = i + 1
            l = 1
            while j < (C - 1) and shadowed[j]:
                grid[l][j] = '/'
                l += 1
                j += 1
            while j < (C - 1) and r > 0:
                grid[l][j] = '/'
                shadowed[j] = True
                r -= 1
                l += 1
                j += 1
    ans = []
    for index in range(1, C):
        row = grid[index]
        include_row = False
        for cell in row:
            if cell == '\\' or cell == '/':
                include_row = True
                break
        if include_row:
            ans.append(row)
        else:
            break
    ans = [['.' for i in range(C)]] + ans
    return len(ans), ans
def lay_right_ramp(i, grid, shadowed):
    pass
def lay_left_ramp(i, grid, shadowed):
    pass
def main():
    T = int(raw_input())
    t = 1
    while t <= T:
        S = int(raw_input())
        B_raw = raw_input().split()
        B = [int(x) for x in B_raw]
        res, grid = solve(B)
        print "Case #{0}: {1}".format(str(t), str(res))
        if grid:
            i = len(grid) - 1
            while i >= 0:
                print ''.join(grid[i])
                i = i - 1
        t += 1
if __name__ == "__main__":
    main()