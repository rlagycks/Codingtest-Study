import sys

def find_index_2d(array, target):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == target:
                return (j)
    return None

input=sys.stdin.readline
expence=[]
DP=[]
anwser=0

N=int(input())
for i in range(N):
    expence.append(list(map(int,input().split())))

for i in range(N):
    if i==0:
        anwser+=min(expence[i])
        DP.append(find_index_2d(expence,min(expence[i])))
    else:
        if find_index_2d(expence,min(expence[i]))==DP[i-1]:
            expence[i][find_index_2d(expence,min(expence[i]))]+=1000
            anwser+=min(expence[i])
            DP.append(find_index_2d(expence,min(expence[i])))
        else:
            anwser+=min(expence[i])
            DP.append(find_index_2d(expence,min(expence[i])))
print(anwser)
