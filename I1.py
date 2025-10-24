import re
from collections import Counter

def count_words_simple(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
        
        words = re.findall(r'\b\w+\b', text)
        
        total_words = len(words)
        print(f"Общее количество слов в файле: {total_words}")
        
        if total_words == 0:
            print("Файл пуст")
            return
        
        word_counter = Counter(words)
        most_common = word_counter.most_common(1)[0]
        
        print(f"Самое частое слово: '{most_common[0]}' (встречается {most_common[1]} раз)")
            
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

filename = 'article.txt'
count_words_simple(filename)