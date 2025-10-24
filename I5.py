with open('dictionary.txt') as f:
    dictionary = set(f.read().splitlines())

text = input()
words = text.split()

result = []
for word in words:
    clean_word = ''.join(c for c in word if c.isalpha())
    if clean_word.lower() in dictionary:
        result.append(word)
    else:
        result.append(f'[{word}]')

print(' '.join(result))