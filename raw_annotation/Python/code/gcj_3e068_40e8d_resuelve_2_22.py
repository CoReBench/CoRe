import sys
def resuelve(N,disp,cuentas):
    pasados = 0
    while(pasados < N):
        pasados += 1
        devolver = "-1"
        flavours = map(int, raw_input().strip().split(" "))
        D = flavours[0]
        if(D != 0):
            posibles = []
            for el in flavours[1:]:
                if(el < N):
                    cuentas[el] += 1
                    if(disp[el] == True):
                        posibles.append((cuentas[el],el))
            if(len(posibles) > 0):
                maxi,elmax = min(posibles)
                devolver = str(elmax)
                disp[elmax] = False
        sys.stdout.write(devolver+"\n")
        sys.stdout.flush()
    return
def solve(N):
    disp = [True for i in range(0,N)]
    cuenta = [0 for i in range(0,N)]
    resuelve(N,disp,cuenta)
    return
if __name__ == "__main__":
    T = input()
    vendidos = 0
    while(vendidos < int(T)):
        vendidos += 1
        a = input()
        solve(int(a))
    exit()