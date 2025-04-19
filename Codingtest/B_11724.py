import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
grap = {}

for _ in range(M):
    u, v = map(int, input().split())
    grap[u] = grap.get(u, []) + [v]
    grap[v] = grap.get(v, []) + [u]

visited = [False] * (N + 1)

def dfs(node):
    visited[node] = True
    for neighbor in grap.get(node, []):
        if not visited[neighbor]:
            dfs(neighbor)

count = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)