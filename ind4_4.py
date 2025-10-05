def calculate_average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

if __name__ == "__main__":
    result = calculate_average(1, 2, 3, 4, 5)
    print(f"Среднее арифметическое: {result}")