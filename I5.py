class NegativeAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise NegativeAgeError("Возраст не может быть отрицательным")
    return f"Возраст {age} корректен"

def process_user_data(name, age):
    try:
        result = check_age(age)
        return f"{name}: {result}"
    except NegativeAgeError as e:
        return f"{name}: Ошибка - {e}"

if __name__ == "__main__":
    print(process_user_data("Иван", 25))
    print(process_user_data("Анна", -5))
    print(process_user_data("Петр", 30))