N, C, W = map(int, input().split())
woods = [int(input()) for _ in range(N)]

max_money = 0
max_l = max(woods)

for l in range(1, max_l + 1):
    profit_sum = 0

    for wood in woods:       
        q, r = divmod(wood, l)

        if r:
            expense = q * C
        else:
            expense = (q - 1) * C
        profit = (q * l * W) - expense

        if profit < 0:
            continue 

        profit_sum += profit

    if profit_sum >= max_money:
        max_money = profit_sum

print(max_money)
