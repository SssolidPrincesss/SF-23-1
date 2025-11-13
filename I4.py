class SimpleLogger:
    def __init__(self, func_name="Функция"):
        self.func_name = func_name
        print(f"Создан декоратор для: {self.func_name}")
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"ВЫЗОВ: {self.func_name} ({func.__name__})")
            print(f"Аргументы: args={args}, kwargs={kwargs}")
            
            result = func(*args, **kwargs)
            
            print(f"РЕЗУЛЬТАТ: {self.func_name} вернула: {result}")
            print(f"---")
            return result
        
        return wrapper

@SimpleLogger("Калькулятор суммы")
def calculate_sum(a, b):
    return a + b

@SimpleLogger("Генератор приветствия")
def create_greeting(name, age):
    return f"Привет, {name}! Тебе {age} лет."

if __name__ == "__main__":
    print("ЗАПУСК ПРОГРАММЫ")
    print("=" * 40)
    
    result1 = calculate_sum(5, 3)
    result2 = create_greeting("Анна", 25)
    result3 = calculate_sum(10, 20)
    
    print(f"Итоговые результаты:")
    print(f"Сумма: {result1}")
    print(f"Приветствие: {result2}")
    print(f"Еще сумма: {result3}")