import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

min_triangle = [min(one), min(two), min(three)]
max_triangle = [max(one), max(two), max(three)]

def triangle_area(sides):
    a, b, c = sides
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

area_min = triangle_area(min_triangle)
area_max = triangle_area(max_triangle)

print("Площадь треугольника из минимальных элементов:", round(area_min, 2))
print("Площадь треугольника из максимальных элементов:", round(area_max, 2))