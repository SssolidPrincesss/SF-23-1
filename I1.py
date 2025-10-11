
checks = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 
          3365, 1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666, 5410, 
          7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928, 5837, 8201, 2643, 5017, 9682,
            8530, 3250, 7193, 9051, 4506, 1987, 3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]


total_checks = len(checks)


unique_visitors = len(set(checks))


from collections import Counter
visitor_counts = Counter(checks)
most_frequent_visitor, max_visits = visitor_counts.most_common(1)[0]

print("=== СТАТИСТИКА ПОСЕЩЕНИЙ РЕСТОРАНА ЗА НЕДЕЛЮ ===")
print(f"Всего выдано чеков: {total_checks}")
print(f"Уникальных посетителей: {unique_visitors}")
print(f"Самый частый посетитель: работник №{most_frequent_visitor} (посетил {max_visits} раз)")
print("\nТоп-5 самых частых посетителей:")
for i, (visitor, count) in enumerate(visitor_counts.most_common(5), 1):
    print(f"{i}. Работник №{visitor} - {count} посещений")