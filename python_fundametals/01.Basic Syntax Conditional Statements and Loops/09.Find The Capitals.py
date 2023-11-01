data = input()


def capital_indexes(string):
    return [i for i, char in enumerate(string) if char.isupper()]


print(capital_indexes(data))
