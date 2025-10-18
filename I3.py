from collections import Counter

def countDigits(nums):
    digit_count = Counter(int(char) for char in nums)

    top_three = dict(digit_count.most_common(3))

    for digit in sorted(top_three.keys()):
        print(f"Цифра {digit}: {top_three[digit]} раз")
    
    return top_three

nums = "123456789012345678901234567890"
result = countDigits(nums)
print("\nСловарь трех самых частых цифр:", result)