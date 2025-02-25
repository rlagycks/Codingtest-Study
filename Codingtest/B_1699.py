import math

def rot(n,r):
    cot=0
    while True:
        lis=[]
        if n>=(r**2):
            n-=(r**2)
            cot+=1
        elif n<(r**2):
            if n<=0:
                break
            else:
                r-=1
    return(cot)

N=int(input())
root=int(math.sqrt(N))
count=0
li=[]
for i in range(root):
    li.append(rot(N,root-i))
print(min(li))