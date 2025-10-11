grades1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def fix_grades(grades):
    result = []
    for grade in grades:
        if grade == 2:
            continue
        elif grade == 3:
            result.append(4)
        else:
            result.append(grade)
    return result

fixed1 = fix_grades(grades1)
fixed2 = fix_grades(grades2)
fixed3 = fix_grades(grades3)

print("Исправленные оценки 1:", fixed1)
print("Исправленные оценки 2:", fixed2)
print("Исправленные оценки 3:", fixed3)