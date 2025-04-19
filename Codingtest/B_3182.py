N = int(input())
graph = {}
for i in range(1, N + 1):
    graph[i] = int(input())  # 단방향: i → graph[i]

def dfs(start):
    visited = set()
    current = start
    while current not in visited:
        visited.add(current)
        current = graph[current]
    return len(visited)

max_cnt = -1
answer = 0
for i in range(1, N + 1):
    cnt = dfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
        answer = i

print(answer)