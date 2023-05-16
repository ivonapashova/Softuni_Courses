rows, columns = list(map(int, input().split(", ")))

matrix = []
sum_columns = [[] for _ in range(columns)]

for row in range(rows):
    cols = list(map(int, input().split()))
    matrix.append(cols)

    for col in range(columns):
        sum_columns[col].append(cols[col])

[print(sum(cols)) for cols in sum_columns]
