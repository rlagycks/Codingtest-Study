import sys

def array(i):
    if i==0:
        return 1
    if i==1:
        return 0

input=sys.stdin.readline
computer=int(input())
N=int(input())
bras=[]
DP=[1]
for i in range(N):
    bras.append(list(map(int,input().split())))
bras.sort()
for k in range(computer):
    for i in range(len(bras)):
        for j in range(0,2):
            if bras[i][j] in DP:
                if bras[i][array(j)] not in DP:
                    DP.append(bras[i][array(j)])
print(len(DP)-1)