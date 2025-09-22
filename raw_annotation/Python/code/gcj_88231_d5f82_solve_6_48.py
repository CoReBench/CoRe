def construct(digits):
    r = 0
    for i, d in enumerate(digits):
        r += (10 ** i) * d
    return r
def solve(n):
    N = n 
    digits = []
    while n != 0:
        digits.append(n%10)
        n /= 10
    A_digits = []
    B_digits = []
    carry = False
    for i, d in enumerate(digits):
        if d == 4:
            if i + 1 < len(digits) and digits[i + 1] % 2 == 1:
                carry = True
                A_digits.append(7)
                B_digits.append(7)
            else:
                A_digits.append(2)
                B_digits.append(2)
        elif d == 8:
            A_digits.append(1)
            B_digits.append(7)
        elif d % 2 == 0:
            A_digits.append(d/2)
            B_digits.append(d/2)
        elif d == 9 and carry:
            A_digits.append(1)
            B_digits.append(7)
        elif d % 2 == 1 and carry:
            A_digits.append(d/2)
            B_digits.append(d/2)
            carry = False
        elif d % 2 == 7:
            A_digits.append(1)
            B_digits.append(6)
        elif d % 2 == 9:
            A_digits.append(1)
            B_digits.append(8)
        elif d % 2 == 1:
            A_digits.append(d/2)
            B_digits.append(d/2 + 1)
    A = construct(A_digits)
    B = construct(B_digits)
    return A, B
def main():
    T = int(raw_input())
    for i in xrange(T):
        N = int(raw_input())
        A, B = solve(N)
        print("Case #%d: %d %d" % (i+1, A, B))
if __name__ == '__main__':
    main()