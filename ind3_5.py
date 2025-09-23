string = 'hello'
memory = 'world'
counter = 0
values = [0, 2, 4, 6, 8, 10]
while counter != 10:
    if counter in values:
        print(string + memory)
    else:
        print(string)
    if counter > 7:
        print(string + memory)
    counter += 1