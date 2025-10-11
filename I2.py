results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

sorted_results = sorted(results)

best_3 = sorted_results[:3]

worst_3 = sorted_results[-3:]

from_10th = sorted_results[9:]

print("=== РЕЗУЛЬТАТЫ БЕГА ===")
print(f"Все результаты (отсортированные): {sorted_results}")
print()
print(f"Три лучших результата: {best_3}")
print(f"Три худших результата: {worst_3}")
print(f"Все результаты начиная с 10-го: {from_10th}")
print()
print("Детальная информация:")
print(f"Лучший результат: {best_3[0]} сек")
print(f"Худший результат: {worst_3[-1]} сек")
print(f"Средний результат: {sum(results)/len(results):.1f} сек")