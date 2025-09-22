import sys
def Q(n,N):
    n = int(n)
    if (n<=N and str(n)<=str(N)) or (n>N and str(n)>str(N)):
        return "Y"
    else:
        return "N"
def main():
    ans = ""
    print("? "+"1"+"0"*10)
    sys.stdout.flush()
    A = input()
    if A=="Y":
        n = 1
        print("? "+"9"*n)
        sys.stdout.flush()
        A = input()
        while A == "N":
            n+=1
            print("? "+"9"*n)
            sys.stdout.flush()
            A = input()
        print("! "+str(10**(n-1)))
    else:
        l = 0
        r = 10
        S = [""]*11
        S[0] ="Y"
        S[10] ="N"
        while 1:
            m = (l+r)//2
            print("? "+str(10**m))
            sys.stdout.flush()
            A = input()
            if A=="Y":
                if S[m+1]=="N":
                    K = m+1
                    break
                S[m] = "Y"
                l = m
            else:
                if S[m-1]=="Y":
                    K = m
                    break
                S[m] = "N"
                r = m
        l = 1
        r = 9
        S = [""]*10
        S[9] ="Y"
        ashi = "9"*10
        print("? "+ans + str(1) + ashi)
        sys.stdout.flush()
        A = input()
        if A=="Y":
            ans += "1"
        else:
            S[1] = "N"
            while 1:
                m = (l+r)//2
                print("? "+ans + str(m) + ashi)
                sys.stdout.flush()
                A = input()
                if A=="Y":
                    if S[m-1]=="N":
                        ans += str(m)
                        break
                    S[m] = "Y"
                    r = m
                else:
                    if S[m+1]=="Y":
                        ans += str(m+1)
                        break
                    S[m] = "N"
                    l = m
        for i in range(K-1):
            l = 0
            r = 9
            S = [""]*10
            S[9]= "Y"
            print("? " + ans + str(0) + ashi)
            sys.stdout.flush()
            A = input()
            if A=="Y":
                ans += "0"
            else:
                S[0] = "N"
                while 1:
                    m = (l+r)//2
                    print("? " + ans + str(m) + ashi)
                    sys.stdout.flush()
                    A = input()
                    if A=="Y":
                        if S[m-1]=="N":
                            ans += str(m)
                            break
                        S[m] = "Y"
                        r = m
                    else:
                        if S[m+1]=="Y":
                            ans += str(m+1)
                            break
                        S[m] = "N"
                        l = m
        print("! " + ans)
main()