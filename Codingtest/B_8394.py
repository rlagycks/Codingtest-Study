N=int(input())
DP=[0]*(N+1)

DP[0]=0
DP[1]=1
DP[2]=2
for i in range(3,N+1):
    DP[i]=(DP[i-2]+DP[i-1])%10
print(DP[N])