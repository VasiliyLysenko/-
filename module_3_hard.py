def calculate_structure_sum(*data):
    sum_ = 0
    a = data[0]
    for i in a:
        if isinstance(i, int):
            sum_ += i
            continue
        elif isinstance(i, str):
            sum_ += len(i)
            continue
        elif not i:
            continue

        if isinstance(i, list):
            sum_ += calculate_structure_sum(i)
        elif isinstance(i, set):
            sum_ += calculate_structure_sum(i)
        elif isinstance(i, tuple):
            sum_ += calculate_structure_sum(i)
        elif isinstance(i, dict):
            dict_ = dict(i)
            keys_ = list(dict_.keys())
            values_ = list(dict_.values())
            d = keys_ + values_
            sum_ += calculate_structure_sum(d)
    return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)