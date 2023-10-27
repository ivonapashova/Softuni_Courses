initial_energy = int(input())
distance_to_enemy = input()
won_battles = 0

while distance_to_enemy != "End of battle":
    distance_to_enemy = int(distance_to_enemy)

    if initial_energy < distance_to_enemy:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        break

    initial_energy -= distance_to_enemy
    won_battles += 1

    if won_battles % 3 == 0:
        initial_energy += won_battles

    distance_to_enemy = input()

if distance_to_enemy == "End of battle":
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")
