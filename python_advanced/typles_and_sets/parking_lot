number_of_commands = int(input())
parking_lot = set()

for _ in range(number_of_commands):
    direction, plate_number = input().split(", ")
    if direction == "IN":
        parking_lot.add(plate_number)
    if direction == "OUT":
        parking_lot.remove(plate_number)

if len(parking_lot) > 0:
    for plate_number in parking_lot:
        print(plate_number)
else:
    print("Parking Lot is Empty")
