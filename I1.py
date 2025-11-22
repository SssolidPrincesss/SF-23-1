def fib(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b, = b, a + b
        count += 1
    
n = 200
fib_200 = None

for i, num in enumerate(fib(n), 1):
    if i == n:
        fib_200 = num
        break

print(f"200-е число Фибоначчи: {fib_200}")
