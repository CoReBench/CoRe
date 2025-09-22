from io import StringIO
from collections import deque
import sys
def main(inputs):
    h, w = map(int, next(inputs).split())
    mass = [ next(inputs) for _ in range(h) ]
    ans = [[-1 for _ in m] for m in mass]
    for i in range(h):
        for j in range(w):
            if ans[i][j] == -1:
                find_black(mass, ans, i, j)
                pass
            pass
        pass
    print(max(sum(ans, [])))
    pass
def find_black(mass, ans, h, w):
    done = [[False for _ in m] for m in mass]
    q = deque()
    q.append((h, w, []))
    candidate = (-1, 0, [])
    candidate_ans = lambda: ans[candidate[0]][candidate[1]] + len(candidate[2])
    candidate_exists = lambda: (candidate[0] != -1)
    while q:
        h, w, path = q.popleft()
        if candidate[0] != -1 and ans[candidate[0]][candidate[1]] + len(candidate[2]) <= len(path):
            h, w, path = candidate
            for idx, (i, j) in enumerate(reversed(path)):
                ans[i][j] = ans[h][w] + idx + 1
                pass
            return
        if mass[h][w] == '#':
            ans[h][w] = 0
            pass
        if ans[h][w] != -1:
            s0 = ans[h][w] + len(path)
            s1 = ans[candidate[0]][candidate[1]] + len(candidate[2])
            if (candidate[0] == -1) or s0 < s1:
                candidate = (h, w, path[:])
                pass
            done[h][w] = True
            continue
        done[h][w] = True
        path.append((h, w))
        if h-1 >= 0 and not done[h-1][w]:
            q.append((h-1, w, path[:]))
            pass
        if h+1 < len(mass) and not done[h+1][w]:
            q.append((h+1, w, path[:]))
            pass
        if w-1 >= 0 and not done[h][w-1]:
            q.append((h, w-1, path[:]))
            pass
        if w+1 < len(mass[0]) and not done[h][w+1]:
            q.append((h, w+1, path[:]))
            pass
        pass
    pass
def gen_inputs(str_=None):
    inputs = StringIO(str_) if str_ else sys.stdin
    while True:
        a = inputs.readline().rstrip()
        yield a
        pass
    pass
if __name__ == "__main__":
    main(gen_inputs())
    pass