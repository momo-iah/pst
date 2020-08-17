money = int(input())
change = [100, 50, 20, 10, 5, 2, 1]
i = 0
for x in change:
    while money >= x:
        money = money - x
        i = i + 1
    print (i,'from',x)

print(i)


cents = int(input())
coins = [100, 50, 20, 10, 5, 2, 1]
count = 0
for coin in coins:
    while cents >= coin:
        cents = cents - coin
        count = count + 1

print(count)

