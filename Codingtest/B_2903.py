import sys

input=sys.stdin.readline
N=int(input())
an=3
for i in range(1,N):
    an+=(an-1)
print(an**2)