import sys
def input(): return sys.stdin.readline().strip()
def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]
def main():
    N = Z()
    A = []
    for _ in range(N):
        A.append(Z())
    A = sorted(A)
    used = [0] * (N)
    output1 = output2 = 0
    i1 = i2 = 0
    j1, j2 = N-1, N-2
    f1 = f2 = True
    used[i1], used[i2], used[j1], used[j2] = 1, 1, 1, 1
    while f1 or f2:
        if f1: output1 += (A[j1]-A[i1])
        if f2: output1 += (A[j2]-A[i2])
        while used[i1]:
            if i1 == N-1:
                f1 = False
                break
            i1 += 1
        used[i1] = 1
        while used[i2]:
            if i2 == N-1:
                f2 = False
                break
            i2 += 1
        used[i2] = 1
        if f1: 
            output1 += (A[j1]-A[i1])
        if f2: 
            output1 += (A[j2]-A[i2])
        while used[j1]:
            if j1 == 0:
                f1 = False
                break
            j1 -= 1
        used[j1] = 1
        while used[j2]:
            if j2 == 0:
                f2 = False
                break
            j2 -= 1
        used[j2] = 1
    i1, i2 = 0, 1
    j1 = j2 = N-1
    f1 = f2 = True
    used = [0] * (N)
    used[i1], used[i2], used[j1], used[j2] = 1, 1, 1, 1
    while f1 or f2:
        if f1: 
            output2 += (A[j1]-A[i1])
        if f2: 
            output2 += (A[j2]-A[i2])
        while used[j1]:
            if j1 == 0:
                f1 = False
                break
            j1 -= 1
        used[j1] = 1
        while used[j2]:
            if j2 == 0:
                f2 = False
                break
            j2 -= 1
        used[j2] = 1
        if f1: 
            output2 += (A[j1]-A[i1])
        if f2: 
            output2 += (A[j2]-A[i2])
        while used[i1]:
            if i1 == N-1:
                f1 = False
                break
            i1 += 1
        used[i1] = 1
        while used[i2]:
            if i2 == N-1:
                f2 = False
                break
            i2 += 1
        used[i2] = 1
    print(max(output1, output2))
    return
if __name__ == '__main__':
    main()