def solve(kase):
    R, C, H, V = map(int, raw_input().strip().split())
    cakes = []
    for i in xrange(R):
        row = list(raw_input().strip())
        cakes.append(row)
    chips = []
    chip_rows = [0] * R
    chip_cols = [0] * C
    chips_cnt = 0
    for i in xrange(R):
        for j in xrange(C):
            if cakes[i][j] == '@':
                chips_cnt += 1
                chip_rows[i] += 1
                chip_cols[j] += 1
    if chips_cnt == 0:
        print "Case #{}: POSSIBLE".format(kase)
        return
    parts = (H + 1) * (V + 1)
    if chips_cnt % parts != 0:
        print "Case #{}: IMPOSSIBLE".format(kase)
        return
    piece_chip = chips_cnt / parts
    rows_chips = piece_chip * (V + 1)
    cols_chips = piece_chip * (H + 1)
    hcuts = [0]
    vcuts = [0]
    chips_row_cnt = 0
    for i in xrange(R):
        chips_row_cnt += chip_rows[i]
        if chips_row_cnt < rows_chips:
            continue
        elif chips_row_cnt == rows_chips:
            chips_row_cnt = 0
            hcuts.append(i + 1)
        else:
            print "Case #{}: IMPOSSIBLE".format(kase)
            return
    chips_col_cnt = 0
    for i in xrange(C):
        chips_col_cnt += chip_cols[i]
        if chips_col_cnt < cols_chips:
            continue
        elif chips_col_cnt == cols_chips:
            chips_col_cnt = 0
            vcuts.append(i + 1)
        else:
            print "Case #{}: IMPOSSIBLE".format(kase)
            return
    for x in xrange(H):
        chips.append([])
        for y in xrange(V):
            chips[x].append(0)
            for i in xrange(hcuts[x], hcuts[x+1]):
                for j in xrange(vcuts[y], vcuts[y+1]):
                    if cakes[i][j] == "@":
                        chips[x][y] += 1
            if chips[x][y] != piece_chip:
                print "Case #{}: IMPOSSIBLE".format(kase)
                return
    print "Case #{}: POSSIBLE".format(kase)
    return
def main():
    T = int(raw_input())
    for kase in xrange(1, T + 1):
        solve(kase)
if __name__ == '__main__':
    main()