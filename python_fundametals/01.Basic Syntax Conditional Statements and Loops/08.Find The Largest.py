number = input()
list_nums = []

for _ in range(len(number)):
    curr_num = int(number)
    divisor = curr_num % 10
    left_digits = curr_num // 10
    number = left_digits
    list_nums.append(divisor)
list_nums.sort(reverse=True)
sorted_number = ''.join((str(n) for n in list_nums))
print(sorted_number)
