import sys
from itertools import combinations

input=sys.stdin.readline
N=int(input())
li=[]
for i in range(N):
    li.append(input())
comb=list(combinations(li,2))

