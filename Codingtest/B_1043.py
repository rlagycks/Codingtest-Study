import sys

input=sys.stdin.readline
N,M=map(int,input().split())
A=input().split()
truth=[]
intruth=[]
for i in range(1,M):
    for j in range(intruth[i][0]):
        intruth.append(input().split())
        if intruth[i] not in truth:
            truth.append(intruth[i])
        elif truth:
            pass