sentence = input("Enter a sentence: ")

print("Length:", len(sentence))
print("Lowercase:", sentence.lower())

vowels = sum(1 for char in sentence.lower() if char in 'aeiou')
print("Vowel count:", vowels)

new_sentence = sentence.replace("ugly", "beauty")
print("After replacement:", new_sentence)

print("Starts with 'The':", sentence.startswith("The"))
print("Ends with 'end':", sentence.endswith("end"))
print()