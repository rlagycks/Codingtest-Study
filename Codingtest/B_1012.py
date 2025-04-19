import sys

sys.setrecursionlimit(10**6)
input=sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def DFS(x,y):
    visited[y][x]=True
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0 <= nx < X and 0 <= ny < Y:
            if maps[ny][nx] == 1 and not visited[ny][nx]:
                DFS(nx, ny)

Testcast=int(input())
for i in range(Testcast):
    count =0
    X,Y,loction=map(int,input().split())
    maps=[[0]*X for _ in range(Y)]
    visited=[[False]*X for _ in range(Y)]
    for i in range(loction):
        n,m=map(int,input().split())
        maps[m][n]=1
    for k in range(X):
        for l in range(Y):
            if maps[l][k] == 1 and not visited[l][k]:
                DFS(k, l)
                count += 1   
    print(count)