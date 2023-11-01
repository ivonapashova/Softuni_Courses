budget = int(input())
command = input()
left_budget = budget

while command != 'End':
    price = int(command)
    if left_budget < price:
        print('You went in overdraft!')
        break
    left_budget = left_budget - price
    command = input()
else:
    print('You bought everything needed.')
