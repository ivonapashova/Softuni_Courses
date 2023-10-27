import math

tournament_cnt = int(input())
start_points = int(input())
W = 0
F = 0
SF = 0
total_points = 0

for i in range(1, tournament_cnt + 1):
    stage = input()
    
    if stage == 'W':
        total_points += 2000
        W += 1
        
    if stage == 'F':
        total_points += 1200
        F += 1
        
    if stage == 'SF':
        total_points += 720
        SF += 1

points_after_all_tournaments = start_points + total_points
average_points = math.floor(total_points / tournament_cnt)
percent_win = (W / tournament_cnt) * 100

print(f'Final points: {points_after_all_tournaments}')
print(f'Average points: {average_points}')
print(f'{percent_win:.2f}%')
