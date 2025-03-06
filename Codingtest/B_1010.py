import sys
import math

input=sys.stdin.readline

N = int(input())

for _ in range(N):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)