def fib(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b, = b, a + b
        count += 1
    
n = 200
fib_200 = None

with open("fib.txt", "w", encoding="utf-8") as file:
    for i, num in enumerate(fib(n), 1):
        file.write(f"{num}\n")
        if i == n:
            fib_200 = num

print(f"200-е число Фибоначчи: {fib_200}")