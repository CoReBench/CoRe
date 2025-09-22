from collections import deque
def search(tx, ty, kx, ky, mp):
  direct = ((-1, 0, 1, 0), (1, 0, -1, 0), (0, -1, 0, 1), (0, 1, 0, -1))
  dic = {}
  dic[(tx, ty, kx, ky)] = 0
  que = deque()
  que.append((0, (tx, ty, kx, ky)))
  while que:
    dist, p = que.popleft()
    tx, ty, kx, ky = p
    for dtx, dty, dkx, dky in direct:
      if mp[ty + dty][tx + dtx] == 0:
        ntx = tx + dtx, 
        nty = ty + dty
      else:
        ntx = tx
        nty = ty
      if mp[ky + dky][kx + dkx] == 0:
        nkx = kx + dkx
        nky = ky + dky
      else:
        nkx = kx
        nky = ky
      if (ntx, nty, nkx, nky) not in dic:
        if (ntx, nty) == (nkx, nky):
          if dist + 1 >= 100:
            print("NA")
          else:
            print(dist + 1)
          return
        dic[(ntx, nty, nkx, nky)] = True
        que.append((dist + 1, (ntx, nty, nkx, nky)))
  else:
    print("NA")
def main():
  while True:
    w, h = map(int, input().split())
    if w == 0:
      break
    tx, ty = map(int, input().split())
    kx, ky = map(int, input().split())
    mp = [[1] + list(map(int, input().split())) + [1] for _ in range(h)]
    mp.insert(0, [1] * (w + 2))
    mp.append([1] * (w + 2))
    search(tx, ty, kx, ky, mp)
main()