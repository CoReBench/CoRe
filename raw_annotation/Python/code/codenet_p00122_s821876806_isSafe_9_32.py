import queue
import copy
def makeList(splist,n):
    for i in range(n):
        springs=[]
        springs.append(splist[i*2:i*2+2])
        springs.append(i)
        yield springs
def isSafe(wfs,safe):
    while not wfs.empty():
        flog=wfs.get()
        flogArea=[]
        spn=flog[1]+1
        for i in range(-1,2):
            for j in [-2,2]:
                dx=flog[0][0]+j
                dy=flog[0][1]+i
                if dx>=0 and dx<10 and dy>=0 and dy<10:
                    flogArea.append([[dx,dy],spn])
        for j in range(-1,2):
            for i in [-2,2]:
                dx=flog[0][0]+j
                dy=flog[0][1]+i
                if dx>=0 and dx<10 and dy>=0 and dy<10:
                    flogArea.append([[dx,dy],spn])
        for i in range(len(safe[spn])):
            if safe[spn][i] in flogArea:
                if spn==9:
                    return True
                if spn<9:
                    wfs.put(safe[spn][i])
    return False
while True:
    fx,fy=map(int,input().split())
    if fx==0 and fy==0:
        break
    n=int(input())
    splist=list(map(int,input().split()))
    safe=[]
    k=makeList(splist,n)
    for spring in k:
        temp=[]
        for i in range(-1,2):
            for j in range(-1,2):
                dw=spring[0][0]+i
                dh=spring[0][1]+j
                if dw>=0 and dw<10 and dh>=0 and dh<10:
                    temp.append([[dw,dh],spring[1]])
        safe.append(temp)
    wfs=queue.Queue()
    first=[[fx,fy],-1]
    wfs.put(first)
    if isSafe(wfs,safe):
        print("OK")
    else:
        print("NA")