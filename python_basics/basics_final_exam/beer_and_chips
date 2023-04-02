import math

football_fan = str(input())
budget = float(input())
num_of_bottles = int(input())
num_of_chips = int(input())

beer_price = num_of_bottles * 1.2
chips_price = (math.ceil((0.45 * beer_price)*num_of_chips))
all_price = beer_price + chips_price
price_change =abs(budget - all_price)

if budget >= all_price:
    print(f'{football_fan} bought a snack and has {(price_change):.2f} leva left.')
else:
    print(f'{football_fan} needs {(all_price - budget):.2f} more leva!')
