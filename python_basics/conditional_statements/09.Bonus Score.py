number = int(input())

bonus = 0
bonus2 = 0
bonus3 = 0

if number <= 100:
    bonus = 5

elif number > 1000:
    bonus = number * 0.10

elif number > 100:
    bonus = number * 0.20

if number % 2 == 0:
    bonus2 = 1

if number % 10 == 5:
    bonus3 = 2

total_bonus = bonus + bonus2 + bonus3
total_number = number + bonus + bonus2 + bonus3

print(total_bonus)
print(total_number)
