def useless(lst):
    return max(lst) / len(lst)

print(useless([3, 5, 7, 3, 33]))
print(useless([-12.5, 56, 77.3, 0, -36, 98.2, -65, 21.7, 47, 89.6]))
print(useless([-26.6, 86, 12.5, -56, 75.2, 0, 65, -91.5, 65.9, -7]))