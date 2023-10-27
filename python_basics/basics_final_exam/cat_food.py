cat_num = int(input())

food_kg = 0
group_one = 0
group_two = 0
group_three = 0
for i in range (0,cat_num):
  grams_food = float(input())
  if grams_food >=100 and grams_food<200:
      group_one += 1
      food_kg += grams_food
  elif grams_food >=200 and grams_food<300:
      group_two += 1
      food_kg += grams_food
  elif grams_food >=300 and grams_food<400:
      group_three += 1
      food_kg += grams_food

price = food_kg / 1000 * 12.45
print(f"Group 1: {group_one} cats.")
print(f"Group 2: {group_two} cats.")
print(f"Group 3: {group_three} cats.")
print(f"Price for food per day: {(price):.2f} lv.")
