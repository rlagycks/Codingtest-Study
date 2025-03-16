import sys

input=sys.stdin.readline
N=int(input())
Option=[]
finish=[]
for i in range(N):
    Option.append(input().strip())
    if Option[i][0].upper not in finish:
        finish.append(Option[i][0].upper)
    elif Option[i][0].upper in finish:
        de=Option[i].find(" ")+1
        if Option[i][de] not in finish:
            finish.append(Option[i][de].upper)
        else:
            for j in range(len(Option[i])):
                if Option[i][j].upper not in finish:
                    finish.append(Option[i][j].upper)
                    break
print(finish)

"""n = int(input())

exist = []
for _ in range(n):
    words = list(input().split())

    flag = False 
    for i in range(len(words)):
        if words[i][0].upper() not in exist:
            exist.append(words[i][0].upper())
            flag = True 
            words[i] = '[' + words[i][0] + ']' + words[i][1:]       
            print(' '.join(words)) 
            break 
    
    if not flag:
        for i in range(len(words)):
            check = False 
            for j in range(len(words[i])):
                if words[i][j].upper() not in exist:
                    exist.append(words[i][j].upper())
                    flag = True 
                    check = True 
                    words[i] = words[i][:j] + '[' + words[i][j] + ']' + words[i][j+1:]
                    print(' '.join(words))
                    break 
            if check: break 
    
    if not flag:
        print(' '.join(words))"""