with open('input.txt') as f:
    banned = set(f.read().split())

text = input()

result = []
i = 0
while i < len(text):
    found = False
    for word in banned:
        if text[i:i+len(word)].lower() == word:
            result.append('*' * len(word))
            i += len(word)
            found = True
            break
    if not found:
        result.append(text[i])
        i += 1

print(''.join(result))