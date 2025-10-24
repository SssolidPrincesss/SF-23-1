import datetime

def add_expense(filename):
    print("\nДобавление расхода")
    try:
        amount = float(input("Сумма: "))
        category = input("Категория: ")
        description = input("Описание: ")
        
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"{amount},{category},{description},{date}\n")
        
        print("Расход добавлен")
        
    except ValueError:
        print("Ошибка: сумма должна быть числом")

def show_expenses(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if not lines:
            print("Нет записей о расходах")
            return
        
        total = 0
        print("\nВсе расходы:")
        print("-" * 50)
        
        for i, line in enumerate(lines, 1):
            parts = line.strip().split(',')
            if len(parts) == 4:
                amount, category, description, date = parts
                total += float(amount)
                print(f"{i}. {date} | {category} | {description} | {amount} руб.")
        
        print("-" * 50)
        print(f"Общая сумма: {total:.2f} руб.")
        
    except FileNotFoundError:
        print("Файл с расходами не найден")

def show_statistics(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if not lines:
            print("Нет записей о расходах")
            return
        
        categories = {}
        total = 0
        
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) == 4:
                amount, category, description, date = parts
                amount_float = float(amount)
                total += amount_float
                
                if category in categories:
                    categories[category] += amount_float
                else:
                    categories[category] = amount_float
        
        print("\nСтатистика:")
        print(f"Всего записей: {len(lines)}")
        print(f"Общая сумма: {total:.2f} руб.")
        
        if categories:
            print("\nПо категориям:")
            for category, amount in categories.items():
                print(f"  {category}: {amount:.2f} руб.")
                
    except FileNotFoundError:
        print("Файл с расходами не найден")

def main():
    filename = "expenses.txt"
    
    while True:
        print("\nУчет расходов")
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Показать статистику")
        print("4. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            add_expense(filename)
        elif choice == '2':
            show_expenses(filename)
        elif choice == '3':
            show_statistics(filename)
        elif choice == '4':
            print("Выход")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()