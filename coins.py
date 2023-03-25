coins = 20
found_coins = 20
magic_coins = 70
stolen_coins = 3
for week in range(1, 53):
    coins = coins + magic_coins - stolen_coins
    print('Week %s = %s' % (week, coins))