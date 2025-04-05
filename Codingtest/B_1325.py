import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grap = {}
counts = []

for _ in range(M):
    A, B = map(int, input().split())
    grap[A] = grap.get(A, []) + [B]
    grap[B] = grap.get(B, []) + [A]

def dfs(node, visited):
    visited[node] = True
    count = 1
    for neighbor in grap.get(node, []):
        if not visited[neighbor]:
            count += dfs(neighbor, visited)
    return count

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    counts.append(dfs(i, visited))

print(counts.index(max(counts)))