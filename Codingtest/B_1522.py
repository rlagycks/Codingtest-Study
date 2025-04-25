String=input()
Counta=String.count('a')
String+=String[0:Counta-1]
min_val = float('inf')
for i in range(len(String)-(Counta-1)):
    min_val = min(min_val,String[i:i+Counta].count('b'))
print(min_val)

