first_numbers = set(map(int, input().split()))  # [1, 2, 3, 4, 5]
second_numbers = set(map(int, input().split()))  # [1, 2, 3]
lines = int(input())

for c in range(lines):
    command = input().split() # ['Add', 'First', '5', '6']
    if command[0] == "Add":
        if command[1] == "First":
            for num in range(len(command) - 2):
                first_numbers.add(int(command.pop())) # {1, 2, 3, 4, 5, 6}

        elif command[1] == "Second":
            for num in range(len(command) - 2):
                second_numbers.add(int(command.pop()))
    elif command[0] == "Remove":
        if command[1] == "First":
            numbers_to_be_removed = set()
            for num in range(len(command) - 2):
                numbers_to_be_removed.add(int(command.pop()))
            first_numbers = first_numbers.difference(numbers_to_be_removed)

        elif command[1] == "Second":
            numbers_to_be_removed = set()
            for num in range(len(command) - 2):
                numbers_to_be_removed.add(int(command.pop()))
            second_numbers = second_numbers.difference(numbers_to_be_removed)

    elif command[0] == "Check":
        diff = second_numbers.issubset(first_numbers)
        if diff:
            print("True")
        else:
            print("False")

sorted_first_numbers = sorted(first_numbers)
sorted_second_numbers = sorted(second_numbers)

print(*sorted_first_numbers, sep=", ")
print(*sorted_second_numbers, sep=", ")
