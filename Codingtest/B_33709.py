import re

N=int(input())
slogon=input()
anser=[]
for slogon in re.split('[|:#.]',slogon):
    anser.append(int(slogon))
print(sum(anser))