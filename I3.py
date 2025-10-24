with open('input.txt', 'r') as f:
    lines = f.readlines()

letter_count = 0
word_count = 0
line_count = len(lines)

for line in lines:
    for char in line:
        if char.isalpha():
            letter_count += 1
    words = line.split()
    word_count += len(words)

print(letter_count, 'letters')
print(word_count, 'words')
print(line_count, 'lines')