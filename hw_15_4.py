
lst1 = [
    {'name': 'Jenifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}
]

max1 = max(lst1, key=lambda v: v['final'])
print(max1)
min1 = min(lst1, key=lambda v: v['final'])
print(min1)

