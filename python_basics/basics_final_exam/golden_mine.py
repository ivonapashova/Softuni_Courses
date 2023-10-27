expected_gold = float(input())
num_of_days = int(input())
gold_for_the_day = float(input())

if expected_gold <= gold_for_the_day:
    print(f"Good job! Average gold per day: {среден добив на ден за дадената локация}.")
else:
    print(f"You need {expected_gold - gold_for_the_day} gold.")
