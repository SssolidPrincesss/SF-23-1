nums = input("Введите последовательность чисел через пробел: ")
nList = [int(x) for x in nums.split()]
nTuple = tuple(nList)
print(nList)
print(nTuple)