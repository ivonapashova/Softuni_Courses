browser_open_cnt = int(input())
salary = int(input())

for i in range(1, browser_open_cnt + 1):
    opened_website = input()
    if opened_website == 'Facebook':
        salary = salary - 150
    elif opened_website == 'Instagram':
        salary = salary - 100
    elif opened_website == 'Reddit':
        salary = salary - 50
if salary <= 0:
    print('You have lost your salary.')
else:
    print(salary)
