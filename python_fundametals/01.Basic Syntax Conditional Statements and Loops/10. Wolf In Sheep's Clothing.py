command = input().split(', ')
length = len(command)

for num in range(1, length + 1):
    curr_command = command[0]
    command.remove(command[0])
    if num == length and curr_command == 'wolf':
        print('Please go away and stop eating my sheep')
    elif curr_command == 'wolf':
        print(f'Oi! Sheep number {length - num}! You are about to be eaten by a wolf!')
