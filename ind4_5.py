from geometry import heron_triangle_area

a = float(input("Введите первую сторону треугольника: "))
b = float(input("Введите вторую сторону треугольника: "))
c = float(input("Введите третью сторону треугольника: "))

area = heron_triangle_area(a, b, c)
print(f"Площадь треугольника: {area}")