def read_file_simple(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        if content.strip() == "":
            raise ValueError("Файл пустой")
        else:
            print(f"Содержимое файла '{filename}':")
            print(content)

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    print("=== Файл с данными ===")
    read_file_simple('data.txt')

    print("\n=== Пустой файл ===")
    read_file_simple('empty.txt')