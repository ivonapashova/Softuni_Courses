word = input().lower()
counter = 0
sand = 'sand'
water = 'water'
fish = 'fish'
sun = 'sun'

if sand in word:
    counter += word.count(sand)
if water in word:
    counter += word.count(water)
if fish in word:
    counter += word.count(fish)
if sun in word:
    counter += word.count(sun)
print(counter)
