num_of_cities = int(input())
city_name = str(input())
income = float(input())
expenses = float(input())

def calculate_profit(num_cities, city_data):
    total_profit = 0
    special_event_counter = 0

    for i in range(num_cities):
        city_name, income, expenses = city_data[i]
        if (i+1) % 3 == 0 and (i+1) % 5 != 0:
            special_event_counter += 1
            expenses *= 1.5
        if (i+1) % 5 == 0 and city_name != "Rainy City":
            income *= 0.9
        profit = income - expenses
        total_profit += profit
    return total_profit

    print(f"In {city_name} Burger Bus earned {profit} leva.")
    print(f"Burger Bus total profit: {total_profit} leva.")
