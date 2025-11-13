def add_two():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)
        result = 2 + number
        print(f"Результат: 2 + {number} = {result}")
        return result
        
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")
        return None


def run_tests():
    print("Тест 1: Ввод целого числа")
    result1 = add_two()
    print(f"Результат теста: {result1}\n")

    print("Тест 2: Ввод дробного числа")
    result2 = add_two()
    print(f"Результат теста: {result2}\n")
    
    print("Тест 3: Ввод строки")
    result3 = add_two()
    print(f"Результат теста: {result3}\n")
    
    print("Тест 4: Ввод специальных символов")
    result4 = add_two()
    print(f"Результат теста: {result4}\n")
    
    print("Тест 5: Ввод отрицательного числа")
    result5 = add_two()
    print(f"Результат теста: {result5}\n")

if __name__ == "__main__":
    print("Функция сложения числа 2 с пользовательским вводом")
    print("=" * 50)

    run_tests()