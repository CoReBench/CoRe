import sys
import numpy as np
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
def main():
    T = int(raw_input())     
    for i in xrange(1, T + 1):
        tmp = raw_input()
        tmpList = map(int, tmp.split())
        N = int(tmpList[0])                          
        K = int(tmpList[1])                          
        stall_occupied = [True]                 
        for j in xrange(N):
            stall_occupied.append(False)
        stall_occupied.append(True)
        Ls = []
        Rs = []
        Min_s = []
        Max_s = []
        for j in xrange(N+2):
            if stall_occupied[j]:
                Ls.append(-1)
                Rs.append(-1)
            else:
                Ls.append(j - 1)
                Rs.append(N - j)
            Min_s.append(min(Ls[-1], Rs[-1]))
            Max_s.append(max(Ls[-1], Rs[-1]))
        for k in xrange(K):
            maximal = max(Min_s)
            if Min_s.count(maximal) > 1:
                values = np.array(Min_s)
                idxs = np.where(values == maximal)[0]
                max_of_idxs = []
                for j in idxs:
                    max_of_idxs.append(Max_s[j])
                max_max = max(max_of_idxs)
                if(max_of_idxs.count(max_max) > 1):
                    values1 = np.array(max_of_idxs)
                    idxs1 = np.where(values1 == max_max)[0]
                    idx = idxs[idxs1[0]]
                else:
                    idx = idxs[max_of_idxs.index(max_max)]
                y =  max(Ls[idx], Rs[idx])
                z =  min(Ls[idx], Rs[idx])
                stall_occupied[idx] = True
                Ls[idx] = -1
                Rs[idx] = -1
                Min_s[idx] = -1
                Max_s[idx] = -1
                leftIdx = idx - 1
                while leftIdx > 0:
                    if stall_occupied[leftIdx]:
                        break
                    Rs[leftIdx] = idx - leftIdx - 1
                    Min_s[leftIdx] = min(Rs[leftIdx], Ls[leftIdx])
                    Max_s[leftIdx] = max(Rs[leftIdx], Ls[leftIdx])
                    leftIdx -= 1
                rightIdx = idx + 1
                while rightIdx < N + 2:
                    if stall_occupied[rightIdx]:
                        break
                    Ls[rightIdx] = rightIdx - idx - 1
                    Min_s[rightIdx] = min(Rs[rightIdx], Ls[rightIdx])
                    Max_s[rightIdx] = max(Rs[rightIdx], Ls[rightIdx])
                    rightIdx += 1
            else:
                idx = Min_s.index(maximal)
                y =  max(Ls[idx], Rs[idx])
                z =  min(Ls[idx], Rs[idx])
                stall_occupied[idx] = True
                Ls[idx] = -1
                Rs[idx] = -1
                Min_s[idx] = -1
                Max_s[idx] = -1
                leftIdx = idx - 1
                while leftIdx > 0:
                    if stall_occupied[leftIdx]:
                        break
                    Rs[leftIdx] = idx - leftIdx - 1
                    Min_s[leftIdx] = min(Rs[leftIdx], Ls[leftIdx])
                    Max_s[leftIdx] = max(Rs[leftIdx], Ls[leftIdx])
                    leftIdx -= 1
                rightIdx = idx + 1
                while rightIdx < N + 2:
                    if stall_occupied[rightIdx]:
                        break
                    Ls[rightIdx] = rightIdx - idx - 1
                    Min_s[rightIdx] = min(Rs[rightIdx], Ls[rightIdx])
                    Max_s[rightIdx] = max(Rs[rightIdx], Ls[rightIdx])
                    rightIdx += 1
        print("Case #{}: {} {}".format(i, y, z))
        sys.stdout.flush()
if __name__ == "__main__":
    main()